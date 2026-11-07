"""Small filesystem and network safety helpers."""
from __future__ import annotations
import os, tempfile
from pathlib import Path
from urllib.parse import urlparse

LOCAL_HOSTS = {"127.0.0.1", "localhost", "::1"}

def require_regular_file(path: Path) -> Path:
    raw = Path(path).expanduser()
    if raw.is_symlink():
        raise ValueError(f"Refusing symlink input: {raw}")
    resolved = raw.resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Not a regular file: {resolved}")
    return resolved

def prepare_output_path(path: Path, source: Path | None = None) -> Path:
    """Return a new output path without following existing symlink components."""
    raw = Path(path).expanduser()
    if not raw.is_absolute():
        raw = Path.cwd() / raw
    raw = Path(os.path.abspath(raw))
    for component in (raw, *raw.parents):
        if component.is_symlink():
            raise ValueError(f"Refusing symlink output path component: {component}")
    if source is not None and raw == Path(source).resolve(strict=True):
        raise ValueError("Output must not overwrite the source file")
    if raw.exists():
        raise FileExistsError(f"Output already exists: {raw}")
    raw.parent.mkdir(parents=True, exist_ok=True)
    # Recheck after creating the parent to catch a symlink introduced in the path.
    for component in (raw.parent, *raw.parent.parents):
        if component.is_symlink():
            raise ValueError(f"Refusing symlink output path component: {component}")
    if raw.exists() or raw.is_symlink():
        raise FileExistsError(f"Output appeared during preparation: {raw}")
    return raw

def write_text_no_overwrite(path: Path, content: str) -> Path:
    """Atomically create a UTF-8 file, refusing existing files and symlink paths."""
    output = prepare_output_path(path)
    fd, temp_name = tempfile.mkstemp(prefix=".afk-text-", dir=output.parent)
    temp = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.link(temp, output)
    finally:
        temp.unlink(missing_ok=True)
    return output

def validate_local_url(url: str, allow_remote: bool = False) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Endpoint must be an http(s) URL with a hostname")
    if parsed.username or parsed.password:
        raise ValueError("Credentials in endpoint URLs are not allowed; use the provider's secure auth flow")
    if parsed.query or parsed.fragment:
        raise ValueError("Endpoint query strings and fragments are not allowed; do not embed tokens in URLs")
    if not allow_remote and parsed.hostname not in LOCAL_HOSTS:
        raise ValueError("Remote endpoints are blocked by default; pass --allow-remote only after reviewing the data destination")
    if parsed.hostname not in LOCAL_HOSTS and parsed.scheme != "https":
        raise ValueError("Remote endpoints must use HTTPS")
    return url.rstrip("/")
