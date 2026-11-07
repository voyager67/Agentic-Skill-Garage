"""Local raster inspection, resizing and contact sheets (optional Pillow extra)."""
from __future__ import annotations
import os, tempfile
from pathlib import Path
from .security import require_regular_file, prepare_output_path

def _pillow():
    try:
        from PIL import Image, ImageOps, ImageDraw
    except ImportError as exc:
        raise RuntimeError("Image commands require Pillow. Install with: pip install -e '.[images]'") from exc
    return Image, ImageOps, ImageDraw

def _destination(path: Path, source: Path|None=None) -> Path:
    return prepare_output_path(Path(path), source=source)

def _save(image, out: Path, fmt: str|None=None, quality: int=92):
    fd,tmp_name=tempfile.mkstemp(prefix=".afk-image-",suffix=out.suffix,dir=out.parent); os.close(fd); tmp=Path(tmp_name)
    try:
        save_format=fmt or out.suffix.lstrip(".").upper()
        if save_format=="JPG": save_format="JPEG"
        if save_format in {"JPEG","WEBP"}: image.save(tmp,format=save_format,quality=quality,optimize=True)
        else: image.save(tmp,format=save_format,optimize=True)
        if out.exists() or out.is_symlink(): raise FileExistsError(out)
        os.link(tmp,out)
    finally:
        tmp.unlink(missing_ok=True)

def inspect(path: Path):
    Image,_,_= _pillow(); src=require_regular_file(Path(path))
    with Image.open(src) as im:
        return {"path":src.name,"format":im.format,"width":im.width,"height":im.height,"mode":im.mode,"has_alpha":("A" in im.getbands()) or "transparency" in im.info,"frames":getattr(im,"n_frames",1)}

def resize(source: Path, output: Path, width: int, height: int, fit: str="contain", allow_upscale: bool=False, background: str="#00000000", quality: int=92):
    Image,ImageOps,_=_pillow(); src=require_regular_file(Path(source)); out=_destination(output,src)
    if not (1<=width<=16384 and 1<=height<=16384): raise ValueError("width and height must be between 1 and 16384")
    if not (1<=quality<=100): raise ValueError("quality must be between 1 and 100")
    if fit not in {"contain","cover"}: raise ValueError("fit must be contain or cover")
    with Image.open(src) as opened:
        im=ImageOps.exif_transpose(opened).copy()
    if not allow_upscale and (im.width<width or im.height<height):
        # For contain, one dimension may be smaller by design. Compare the scale factor.
        scale=min(width/im.width,height/im.height) if fit=="contain" else max(width/im.width,height/im.height)
        if scale>1: raise ValueError("Requested size would upscale the source; pass --allow-upscale to confirm")
    if fit=="contain":
        im.thumbnail((width,height),Image.Resampling.LANCZOS)
        canvas=Image.new("RGBA",(width,height),background if background else (0,0,0,0))
        if im.mode!="RGBA": im=im.convert("RGBA")
        canvas.alpha_composite(im,((width-im.width)//2,(height-im.height)//2)); result=canvas
    else:
        if im.mode not in {"RGB","RGBA"}: im=im.convert("RGBA" if "A" in im.getbands() else "RGB")
        result=ImageOps.fit(im,(width,height),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    if out.suffix.lower() in {".jpg",".jpeg"} and result.mode=="RGBA":
        bg=Image.new("RGB",result.size,(255,255,255)); bg.paste(result,mask=result.getchannel("A")); result=bg
    _save(result,out,quality=quality)
    return {"output":str(out),"width":result.width,"height":result.height,"format":out.suffix.lstrip(".").lower(),"fit":fit,"source":src.name}

def contact_sheet(sources: list[Path], output: Path, cell_width: int=320, cell_height: int=240, columns: int=3, gap: int=18, background: str="#20242b"):
    Image,ImageOps,ImageDraw=_pillow()
    if not sources: raise ValueError("Provide at least one image")
    if len(sources)>200: raise ValueError("Contact sheets are limited to 200 images")
    if not (64<=cell_width<=2048 and 64<=cell_height<=2048 and 1<=columns<=10 and 0<=gap<=128): raise ValueError("Invalid contact sheet dimensions")
    paths=[require_regular_file(Path(x)) for x in sources]
    out=_destination(output)
    columns=min(columns,len(paths)); rows=(len(paths)+columns-1)//columns; label_h=34
    sheet=Image.new("RGB",(gap+columns*(cell_width+gap),gap+rows*(cell_height+label_h+gap)),background)
    draw=ImageDraw.Draw(sheet)
    for index,path in enumerate(paths):
        with Image.open(path) as opened: im=ImageOps.exif_transpose(opened).convert("RGB")
        im.thumbnail((cell_width,cell_height),Image.Resampling.LANCZOS)
        x=gap+(index%columns)*(cell_width+gap); y=gap+(index//columns)*(cell_height+label_h+gap)
        sheet.paste(im,(x+(cell_width-im.width)//2,y+(cell_height-im.height)//2))
        label=path.name[:44]
        draw.text((x,y+cell_height+8),label,fill="#f3f4f6")
    _save(sheet,out,quality=92)
    return {"output":str(out),"images":len(paths),"width":sheet.width,"height":sheet.height}
