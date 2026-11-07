"""Blender headless scene audit and no-overwrite still rendering."""
from __future__ import annotations
import json, os, shutil, subprocess, tempfile
from pathlib import Path
from .security import require_regular_file, prepare_output_path

AUDIT_EXPR = "import bpy,json; s=bpy.context.scene; objs=list(s.objects); data={\"blender_version\":bpy.app.version_string,\"scene\":s.name,\"objects\":len(objs),\"meshes\":sum(o.type==\"MESH\" for o in objs),\"cameras\":sum(o.type==\"CAMERA\" for o in objs),\"lights\":sum(o.type==\"LIGHT\" for o in objs),\"frame_start\":s.frame_start,\"frame_end\":s.frame_end,\"resolution\":[s.render.resolution_x,s.render.resolution_y,s.render.resolution_percentage],\"engine\":s.render.engine}; print(\"ASG_SCENE_JSON=\"+json.dumps(data,sort_keys=True))"

def _blender():
    path=shutil.which("blender")
    if not path: raise RuntimeError("Blender is not installed or not on PATH")
    return path

def audit(path: Path):
    source=require_regular_file(Path(path))
    cmd=[_blender(),"--background","--disable-autoexec",str(source),"--python-expr",AUDIT_EXPR]
    result=subprocess.run(cmd,capture_output=True,text=True,check=False)
    if result.returncode: raise RuntimeError(result.stderr[-4000:] or "Blender audit failed")
    marker=next((line.split("ASG_SCENE_JSON=",1)[1] for line in result.stdout.splitlines() if "ASG_SCENE_JSON=" in line),None)
    if marker is None: raise RuntimeError("Blender completed without emitting the scene audit record")
    return json.loads(marker)

def render_still(path: Path, output_prefix: Path, frame: int|None=None):
    source=require_regular_file(Path(path))
    if frame is not None and frame < 0: raise ValueError("frame must be non-negative")
    output_frame=1 if frame is None else frame
    prefix=Path(output_prefix).expanduser()
    expected_raw=Path(f"{prefix}{output_frame:04d}.png")
    expected=prepare_output_path(expected_raw)
    prefix_abs=Path(prefix if prefix.is_absolute() else Path.cwd()/prefix)
    if prefix_abs.is_symlink() or prefix_abs.exists(): raise FileExistsError(f"Render output prefix already exists: {prefix_abs}")
    with tempfile.TemporaryDirectory(prefix=".asg-render-",dir=prefix.parent) as temp_dir:
        temp_prefix=Path(temp_dir)/prefix.name
        cmd=[_blender(),"--background","--disable-autoexec",str(source),"--render-output",str(temp_prefix),"-F","PNG","-f",str(output_frame)]
        result=subprocess.run(cmd,capture_output=True,text=True,check=False)
        if result.returncode: raise RuntimeError(result.stderr[-4000:] or "Blender render failed")
        generated=Path(f"{temp_prefix}{output_frame:04d}.png")
        if not generated.is_file(): raise RuntimeError("Blender completed without creating the expected PNG output")
        if expected.exists() or expected.is_symlink(): raise FileExistsError(f"Render output appeared during processing: {expected}")
        os.link(generated,expected)
    return {"output":str(expected),"bytes":expected.stat().st_size,"frame":output_frame,"stdout_tail":result.stdout[-1200:]}
