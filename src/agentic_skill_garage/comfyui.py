"""Narrow local ComfyUI client with explicit reference upload and job polling."""
from __future__ import annotations
import json, mimetypes, re, secrets, time, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import quote, urlparse
from .security import validate_local_url, require_regular_file, LOCAL_HOSTS

MAX_RESPONSE = 10 * 1024 * 1024
MAX_UPLOAD = 50 * 1024 * 1024

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def _read_json(response):
    raw=response.read(MAX_RESPONSE+1)
    if len(raw)>MAX_RESPONSE: raise RuntimeError("ComfyUI response exceeded the 10 MiB safety limit")
    try: return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError,json.JSONDecodeError): return {"raw_bytes":len(raw)}

def _send(request, base: str, timeout: float):
    try:
        opener = urllib.request.build_opener(_NoRedirect)
        with opener.open(request,timeout=timeout) as response:
            return _read_json(response)
    except urllib.error.HTTPError as exc:
        detail=exc.read(2048).decode("utf-8","replace")
        raise RuntimeError(f"ComfyUI returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach ComfyUI at {base}: {exc.reason}") from exc

def request(base_url: str, path: str, payload: dict|None=None, timeout: float=10.0, allow_remote: bool=False):
    base=validate_local_url(base_url,allow_remote=allow_remote)
    if not path.startswith("/") or ".." in path.split("/"):
        raise ValueError("ComfyUI API path must be an absolute, traversal-free path")
    url=base+path
    data=None if payload is None else json.dumps(payload).encode("utf-8")
    if data is not None and len(data)>5*1024*1024:
        raise ValueError("ComfyUI JSON request payloads are limited to 5 MiB")
    req=urllib.request.Request(url,data=data,headers={"Content-Type":"application/json"},method="GET" if data is None else "POST")
    return _send(req,base,timeout)

def status(base_url: str, allow_remote: bool=False):
    return request(base_url,"/system_stats",allow_remote=allow_remote)

def submit(workflow_path: Path, base_url: str, allow_remote: bool=False):
    source=require_regular_file(Path(workflow_path))
    with source.open("rb") as stream:
        raw=stream.read(5*1024*1024+1)
    if len(raw)>5*1024*1024:
        raise ValueError("ComfyUI workflow files are limited to 5 MiB")
    try:
        workflow=json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError,json.JSONDecodeError) as exc:
        raise ValueError(f"Workflow must be valid UTF-8 JSON: {exc}") from exc
    if not isinstance(workflow,dict) or not workflow:
        raise ValueError("Workflow must be a non-empty ComfyUI API-format JSON object")
    payload=workflow if "prompt" in workflow else {"prompt":workflow}
    if not isinstance(payload.get("prompt"),dict):
        raise ValueError("Workflow prompt must be a JSON object")
    return request(base_url,"/prompt",payload,timeout=30,allow_remote=allow_remote)

def upload_image(source: Path, base_url: str, allow_remote: bool=False):
    """Upload one explicitly selected image to ComfyUI's input folder."""
    path=require_regular_file(Path(source))
    size=path.stat().st_size
    if size>MAX_UPLOAD: raise ValueError("Reference upload is limited to 50 MiB")
    base=validate_local_url(base_url,allow_remote=allow_remote)
    safe_name=re.sub(r"[^A-Za-z0-9._-]+","_",path.name).strip("._") or "reference.bin"
    boundary="----Agentic Skill Garage"+secrets.token_hex(16)
    content_type=mimetypes.guess_type(safe_name)[0] or "application/octet-stream"
    with path.open("rb") as stream:
        data=stream.read(MAX_UPLOAD+1)
    if len(data)>MAX_UPLOAD:
        raise ValueError("Reference upload is limited to 50 MiB")
    if len(data)!=size:
        raise RuntimeError("Reference file changed while it was being read; upload was aborted")
    if not content_type.startswith("image/"):
        raise ValueError("Reference upload must use a recognized image file extension")
    parts=[
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\ninput\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\nfalse\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{safe_name}\"\r\nContent-Type: {content_type}\r\n\r\n".encode(),
        data, f"\r\n--{boundary}--\r\n".encode(),
    ]
    req=urllib.request.Request(base+"/upload/image",data=b"".join(parts),headers={"Content-Type":f"multipart/form-data; boundary={boundary}"},method="POST")
    result=_send(req,base,timeout=60)
    return {"upload":result,"source_name":path.name,"bytes":size,"destination":"ComfyUI input folder","remote":urlparse(base).hostname not in LOCAL_HOSTS}

def wait_for_job(prompt_id: str, base_url: str, timeout: float=600, interval: float=2, allow_remote: bool=False):
    if not re.fullmatch(r"[A-Fa-f0-9-]{8,128}",prompt_id): raise ValueError("prompt_id must be a UUID-like hexadecimal identifier")
    if not 1<=timeout<=3600: raise ValueError("timeout must be between 1 and 3600 seconds")
    if not 0.25<=interval<=30: raise ValueError("poll interval must be between 0.25 and 30 seconds")
    deadline=time.monotonic()+timeout
    while True:
        response=request(base_url,"/history/"+quote(prompt_id,safe=""),timeout=15,allow_remote=allow_remote)
        item=response.get(prompt_id) if isinstance(response,dict) else None
        if isinstance(item,dict):
            state=item.get("status",{})
            if not isinstance(state,dict): state={}
            if state.get("completed"):
                return {"status":"completed","prompt_id":prompt_id,"result":item}
            status_str=state.get("status_str")
            if status_str in {"error","failed"}:
                raise RuntimeError(f"ComfyUI job {prompt_id} failed: {state}")
        remaining=deadline-time.monotonic()
        if remaining<=0: return {"status":"timeout","prompt_id":prompt_id,"timeout_seconds":timeout}
        time.sleep(min(interval,remaining))
