"""FFmpeg/FFprobe operations with argument arrays and non-overwrite defaults."""
from __future__ import annotations
import json, math, os, re, shutil, subprocess, tempfile
from pathlib import Path
from .security import require_regular_file, prepare_output_path

PRESETS={
 "h264-web":["-c:v","libx264","-crf","20","-preset","medium","-c:a","aac","-b:a","192k","-movflags","+faststart"],
 "h265-archive":["-c:v","libx265","-crf","24","-preset","medium","-c:a","aac","-b:a","192k"],
 "webm":["-c:v","libvpx-vp9","-crf","32","-b:v","0","-c:a","libopus"],
 "mp3":["-vn","-c:a","libmp3lame","-q:a","2"],
 "wav":["-vn","-c:a","pcm_s24le"],
}

def _binary(name: str):
    path=shutil.which(name)
    if not path: raise RuntimeError(f"{name} is not installed or not on PATH")
    return path

def probe(path: Path):
    source=require_regular_file(Path(path))
    result=subprocess.run([_binary("ffprobe"),"-v","error","-show_format","-show_streams","-of","json",str(source)],capture_output=True,text=True,check=False)
    if result.returncode: raise RuntimeError(result.stderr.strip() or "ffprobe failed")
    return json.loads(result.stdout)

def _output_path(source: Path, output: Path):
    return prepare_output_path(Path(output), source=source)

def _run_staged_output(command_prefix: list[str], output: Path, failure_message: str):
    """Write beside the destination, then atomically publish without overwriting."""
    with tempfile.TemporaryDirectory(prefix=".asg-media-", dir=output.parent) as staging_dir:
        staged = Path(staging_dir) / output.name
        result = subprocess.run(
            [*command_prefix, str(staged)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            detail = (result.stderr or "").strip()
            raise RuntimeError(detail[-4000:] or failure_message)
        if staged.is_symlink() or not staged.is_file():
            raise RuntimeError("FFmpeg exited successfully without creating its staged output")
        try:
            # A hard link fails atomically if another process created the destination.
            os.link(staged, output)
        except FileExistsError as exc:
            raise FileExistsError(f"Output appeared while processing: {output}") from exc
    return result

def transcode(source: Path, output: Path, preset: str):
    src=require_regular_file(Path(source)); out=_output_path(src,output)
    if preset not in PRESETS: raise ValueError(f"Unknown preset {preset!r}; choose from {', '.join(PRESETS)}")
    command=[_binary("ffmpeg"),"-hide_banner","-nostdin","-n","-i",str(src),*PRESETS[preset],str(out)]
    _run_staged_output(command[:-1],out,"ffmpeg failed")
    return {
        "output":str(out),
        "bytes":out.stat().st_size,
        "command":command,
        "write_strategy":"staged temporary file with atomic no-overwrite promotion",
    }

def measure_loudness(path: Path):
    """Measure integrated loudness, loudness range, and true peak with FFmpeg ebur128."""
    source=require_regular_file(Path(path))
    cmd=[_binary("ffmpeg"),"-hide_banner","-nostats","-nostdin","-i",str(source),"-filter_complex","ebur128=peak=true","-f","null","-"]
    result=subprocess.run(cmd,capture_output=True,text=True,check=False)
    if result.returncode: raise RuntimeError(result.stderr[-4000:] or "FFmpeg loudness measurement failed")
    summary=result.stderr.rsplit("Summary:",1)[-1]
    def number(pattern):
        match=re.search(pattern,summary,re.IGNORECASE|re.MULTILINE)
        if not match: return None
        try: value=float(match.group(1))
        except ValueError: return None
        return value if math.isfinite(value) else None
    integrated=number(r"Integrated loudness:\s*I:\s*(-?(?:\d+(?:\.\d+)?|inf))\s*LUFS")
    lra=number(r"Loudness range:\s*LRA:\s*(-?(?:\d+(?:\.\d+)?|inf))\s*LU")
    true_peak=number(r"True peak:\s*Peak:\s*(-?(?:\d+(?:\.\d+)?|inf))\s*dBFS")
    if integrated is None and lra is None and true_peak is None:
        return {"status":"unavailable","reason":"FFmpeg completed but the ebur128 summary could not be parsed.","source":source.name}
    return {"status":"measured","source":source.name,"integrated_lufs":integrated,"loudness_range_lu":lra,"true_peak_dbfs":true_peak}

def normalize_audio(source: Path, output: Path, target_lufs: float=-16.0):
    if not math.isfinite(target_lufs) or not -30 <= target_lufs <= -10: raise ValueError("target LUFS must be finite and between -30 and -10")
    src=require_regular_file(Path(source)); out=_output_path(src,output)
    filt=f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11"
    command=[_binary("ffmpeg"),"-hide_banner","-nostdin","-n","-i",str(src),"-af",filt,"-ar","48000",str(out)]
    _run_staged_output(command[:-1],out,"ffmpeg failed")
    try:
        measurement=measure_loudness(out)
    except RuntimeError as exc:
        measurement={"status":"unavailable","reason":str(exc)}
    return {
        "output":str(out),
        "bytes":out.stat().st_size,
        "requested_lufs":target_lufs,
        "measurement":measurement,
        "write_strategy":"staged temporary file with atomic no-overwrite promotion",
    }

def extract_frames(source: Path, output_dir: Path, fps: float=1.0):
    if not math.isfinite(fps) or not 0.01 <= fps <= 60: raise ValueError("fps must be finite and between 0.01 and 60")
    src=require_regular_file(Path(source)); raw=Path(output_dir).expanduser()
    if not raw.is_absolute(): raw=Path.cwd()/raw
    out=Path(os.path.abspath(raw))
    for component in (out, *out.parents):
        if component.is_symlink(): raise ValueError(f"Refusing symlink output path component: {component}")
    out.parent.mkdir(parents=True,exist_ok=True)
    for component in (out.parent, *out.parent.parents):
        if component.is_symlink(): raise ValueError(f"Refusing symlink output path component: {component}")
    if out.exists() and not out.is_dir(): raise NotADirectoryError(out)
    if out.exists() and any(out.iterdir()): raise FileExistsError(f"Output directory is not empty: {out}")

    promoted=[]
    with tempfile.TemporaryDirectory(prefix=".asg-frames-",dir=out.parent) as staging_root:
        staged_dir=Path(staging_root)/"frames"
        staged_dir.mkdir()
        pattern=staged_dir/"frame-%06d.jpg"
        command=[_binary("ffmpeg"),"-hide_banner","-nostdin","-n","-i",str(src),"-vf",f"fps={fps}","-q:v","2",str(pattern)]
        result=subprocess.run(command,capture_output=True,text=True,check=False)
        if result.returncode:
            detail=(result.stderr or "").strip()
            raise RuntimeError(detail[-4000:] or "ffmpeg failed")
        frames=sorted(staged_dir.glob("frame-*.jpg"))
        if any(frame.is_symlink() or not frame.is_file() for frame in frames):
            raise RuntimeError("FFmpeg produced an unexpected non-regular frame output")
        if frames:
            if not out.exists():
                try:
                    out.mkdir()
                except FileExistsError as exc:
                    raise FileExistsError(f"Output directory appeared while extracting frames: {out}") from exc
            if out.is_symlink() or not out.is_dir():
                raise ValueError(f"Refusing unsafe frame output directory: {out}")
            for frame in frames:
                destination=out/frame.name
                try:
                    os.link(frame,destination)
                except FileExistsError as exc:
                    raise RuntimeError(
                        f"Frame destination appeared during extraction after {len(promoted)} "
                        f"frame(s) were published: {destination}"
                    ) from exc
                promoted.append(destination)
    return {"output_dir":str(out),"frames":len(promoted),"fps":fps}
