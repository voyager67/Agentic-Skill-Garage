"""Local asset intake, manifests, and duplicate discovery."""
from __future__ import annotations
import hashlib, json, mimetypes, os, shutil, tempfile
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
from .security import require_regular_file

MANIFEST = "manifest.jsonl"

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def _manifest_path(root: Path) -> Path:
    return root / MANIFEST

def _entries(root: Path):
    m=_manifest_path(root)
    if m.is_symlink():
        raise ValueError(f"Refusing symlink manifest: {m}")
    if not m.exists():
        return []
    if not m.is_file():
        raise ValueError(f"Manifest is not a regular file: {m}")
    result=[]
    for number,line in enumerate(m.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip():
            continue
        try: result.append(json.loads(line))
        except json.JSONDecodeError as exc: raise ValueError(f"Invalid manifest line {number}: {exc}") from exc
    return result

def ingest(source: Path, library: Path, relative_path: str|None=None) -> dict:
    source=require_regular_file(Path(source))
    library=Path(library).expanduser().resolve()
    library.mkdir(parents=True,exist_ok=True)
    sha=digest(source)
    existing=next((x for x in _entries(library) if x.get("sha256")==sha),None)
    if existing:
        return {"status":"duplicate","asset":existing}
    rel=PurePosixPath(relative_path or source.name)
    if rel.is_absolute() or not rel.parts or any(part in {".",".."} or "\\" in part or ":" in part for part in rel.parts):
        raise ValueError("Asset destination must be a safe relative path")
    safe_parts=[part for part in rel.parts if part]
    parent=library
    for part in safe_parts[:-1]:
        parent=parent/part
        if parent.is_symlink(): raise ValueError(f"Refusing symlink destination directory: {parent}")
        parent.mkdir(exist_ok=True)
        if not parent.is_dir(): raise NotADirectoryError(parent)
    target=parent/safe_parts[-1]
    if target.exists() or target.is_symlink():
        raise FileExistsError(f"Destination already exists: {target}; source files are never overwritten")
    fd,tmp_name=tempfile.mkstemp(prefix=".afk-",dir=parent)
    os.close(fd)
    tmp=Path(tmp_name)
    try:
        shutil.copyfile(source,tmp)
        # Detect source mutation while copying; the manifest hash must match the stored bytes.
        if digest(tmp) != sha:
            raise RuntimeError("Source changed while it was being copied; intake was aborted")
        # A hard-link creation is atomic and fails rather than replacing an existing path.
        os.link(tmp,target)
    finally:
        if tmp.exists(): tmp.unlink()
    relative=target.relative_to(library).as_posix()
    entry={
        "asset_id":sha[:16],"name":source.name,"path":relative,"sha256":sha,
        "bytes":target.stat().st_size,"media_type":mimetypes.guess_type(target.name)[0] or "application/octet-stream",
        "ingested_at":datetime.now(timezone.utc).isoformat(),"source_name":source.name,
    }
    with _manifest_path(library).open("a",encoding="utf-8") as f:
        f.write(json.dumps(entry,ensure_ascii=False,sort_keys=True)+"\n")
    return {"status":"ingested","asset":entry}

_SKIP_DIRS={".git",".hg",".svn",".venv","venv","node_modules","__pycache__",".cache","build","dist"}

def ingest_many(sources: list[Path], library: Path, recursive: bool=False) -> dict:
    """Ingest explicitly selected files; recurse only when the user opts in."""
    if not sources: raise ValueError("Provide one or more source paths")
    collected=[]
    for raw in sources:
        path=Path(raw).expanduser()
        if path.is_symlink(): raise ValueError(f"Refusing symlink input: {path}")
        if path.is_file():
            collected.append((path,path.name))
            continue
        if not path.is_dir(): raise ValueError(f"Input does not exist or is not a regular file/directory: {path}")
        if not recursive: raise ValueError(f"Directory input requires --recursive: {path}")
        base=path.resolve(strict=True)
        for current,dirs,files in os.walk(base,followlinks=False):
            current_path=Path(current)
            dirs[:]=sorted(d for d in dirs if not d.startswith(".") and d not in _SKIP_DIRS and not (current_path/d).is_symlink())
            for filename in sorted(files):
                file_path=current_path/filename
                if filename.startswith(".") or file_path.is_symlink() or not file_path.is_file(): continue
                rel=PurePosixPath(base.name)/PurePosixPath(file_path.relative_to(base).as_posix())
                collected.append((file_path,rel.as_posix()))
    if not collected: raise ValueError("No eligible files found in the selected inputs")
    library=Path(library).expanduser().resolve()
    library.mkdir(parents=True,exist_ok=True)
    known_hashes={x.get("sha256") for x in _entries(library)}
    planned_hashes=set(known_hashes); planned_paths=set(); conflicts=[]
    for source,relative in collected:
        sha=digest(require_regular_file(source))
        if sha in planned_hashes:
            continue
        rel=PurePosixPath(relative)
        if rel.is_absolute() or not rel.parts or any(part in {".",".."} or "\\" in part or ":" in part for part in rel.parts):
            raise ValueError(f"Unsafe destination path for {source.name}")
        destination=library.joinpath(*rel.parts)
        key=rel.as_posix().casefold()
        if key in planned_paths or destination.exists() or destination.is_symlink(): conflicts.append(rel.as_posix())
        planned_paths.add(key); planned_hashes.add(sha)
    if conflicts: raise FileExistsError("Asset destination collision(s), no files copied: "+", ".join(sorted(set(conflicts))))
    results=[]
    for source,relative in collected:
        try:
            results.append(ingest(source,library,relative))
        except (OSError,ValueError,RuntimeError) as exc:
            return {"status":"partial_failure","files_seen":len(collected),"completed":len(results),"failed_source":source.name,"error":str(exc),"results":results}
    return {"status":"completed","files_seen":len(collected),"ingested":sum(x["status"]=="ingested" for x in results),"duplicates":sum(x["status"]=="duplicate" for x in results),"results":results}

def list_assets(library: Path):
    return _entries(Path(library).expanduser().resolve())

def duplicates(library: Path):
    seen={}; dup=[]
    for entry in _entries(Path(library).expanduser().resolve()):
        sha=entry.get("sha256")
        if sha in seen: dup.append((seen[sha],entry))
        else: seen[sha]=entry
    return dup
