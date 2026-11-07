"""Agentic Skill Garage command-line interface."""
from __future__ import annotations
import argparse, json, os, shutil, sys
from decimal import Decimal, InvalidOperation
from pathlib import Path
from . import __version__
from . import assets, blender, comfyui, identity, image, media, pricing
from .security import write_text_no_overwrite

def _json(data): print(json.dumps(data,indent=2,ensure_ascii=False,default=str))
def _doctor():
    names=["ffmpeg","ffprobe","blender","maya","mayapy","ZBrush","UnrealEditor","Unity","krita","gimp","audacity","magick","ollama"]
    found={n:shutil.which(n) for n in names}
    endpoint=os.environ.get("ASG_COMFYUI_URL","http://127.0.0.1:8188")
    return {"agentic_skill_garage":__version__,"python":sys.version.split()[0],"tools":found,"comfyui_endpoint_configured":bool(os.environ.get("ASG_COMFYUI_URL")),"comfyui_default":"http://127.0.0.1:8188 (loopback only)","note":"Missing applications are optional; no provider calls or data uploads are made by doctor."}

def main(argv=None):
    parser=argparse.ArgumentParser(prog="asg",description="Local-first creative production tools for AI agents and artists")
    parser.add_argument("--version",action="version",version=f"Agentic Skill Garage {__version__}")
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("doctor",help="Detect available local tools; no network or spend")
    a=sub.add_parser("assets",help="Local asset library operations"); a_sub=a.add_subparsers(dest="action",required=True)
    ai=a_sub.add_parser("ingest"); ai.add_argument("sources",nargs="+",type=Path); ai.add_argument("--library",type=Path,default=Path("./asg-assets")); ai.add_argument("--recursive",action="store_true",help="Recursively ingest selected folders; hidden files and common cache folders are skipped")
    al=a_sub.add_parser("list"); al.add_argument("--library",type=Path,default=Path("./asg-assets"))
    ad=a_sub.add_parser("duplicates"); ad.add_argument("--library",type=Path,default=Path("./asg-assets"))
    i=sub.add_parser("identity",help="Create identity profiles and reference prompt packets"); i_sub=i.add_subparsers(dest="action",required=True)
    ii=i_sub.add_parser("init"); ii.add_argument("name"); ii.add_argument("--kind",default="character",choices=["character","brand","product","environment","prop"]); ii.add_argument("--output",type=Path,default=Path("identity.json"))
    ip=i_sub.add_parser("prompt"); ip.add_argument("profile",type=Path); ip.add_argument("--manifest",type=Path,default=Path("./asg-assets/manifest.jsonl")); ip.add_argument("--output",type=Path)
    q=sub.add_parser("quote",help="Estimate from a dated, sourced local rate card; never spends"); q.add_argument("--rate-card",type=Path,required=True); q.add_argument("--provider",required=True); q.add_argument("--model",required=True); q.add_argument("--unit",required=True); q.add_argument("--quantity",required=True)
    c=sub.add_parser("comfyui",help="Interact with a ComfyUI endpoint"); c_sub=c.add_subparsers(dest="action",required=True)
    cs=c_sub.add_parser("status"); cs.add_argument("--url",default=os.environ.get("ASG_COMFYUI_URL","http://127.0.0.1:8188")); cs.add_argument("--allow-remote",action="store_true")
    cr=c_sub.add_parser("submit"); cr.add_argument("workflow",type=Path); cr.add_argument("--url",default=os.environ.get("ASG_COMFYUI_URL","http://127.0.0.1:8188")); cr.add_argument("--allow-remote",action="store_true")
    cu=c_sub.add_parser("upload"); cu.add_argument("source",type=Path); cu.add_argument("--url",default=os.environ.get("ASG_COMFYUI_URL","http://127.0.0.1:8188")); cu.add_argument("--allow-remote",action="store_true")
    cw=c_sub.add_parser("wait"); cw.add_argument("prompt_id"); cw.add_argument("--url",default=os.environ.get("ASG_COMFYUI_URL","http://127.0.0.1:8188")); cw.add_argument("--timeout",type=float,default=600); cw.add_argument("--interval",type=float,default=2); cw.add_argument("--allow-remote",action="store_true")
    im=sub.add_parser("image",help="Local raster operations (requires the images extra)"); im_sub=im.add_subparsers(dest="action",required=True)
    im_info=im_sub.add_parser("info"); im_info.add_argument("source",type=Path)
    im_resize=im_sub.add_parser("resize"); im_resize.add_argument("source",type=Path); im_resize.add_argument("output",type=Path); im_resize.add_argument("--width",type=int,required=True); im_resize.add_argument("--height",type=int,required=True); im_resize.add_argument("--fit",choices=["contain","cover"],default="contain"); im_resize.add_argument("--allow-upscale",action="store_true"); im_resize.add_argument("--background",default="#00000000"); im_resize.add_argument("--quality",type=int,default=92)
    im_sheet=im_sub.add_parser("contact-sheet"); im_sheet.add_argument("sources",nargs="+",type=Path); im_sheet.add_argument("--output",type=Path,required=True); im_sheet.add_argument("--columns",type=int,default=3)
    m=sub.add_parser("media",help="FFmpeg media inspection and conversion"); m_sub=m.add_subparsers(dest="action",required=True)
    mp=m_sub.add_parser("probe"); mp.add_argument("source",type=Path)
    ml=m_sub.add_parser("loudness"); ml.add_argument("source",type=Path)
    mt=m_sub.add_parser("transcode"); mt.add_argument("source",type=Path); mt.add_argument("output",type=Path); mt.add_argument("--preset",choices=["h264-web","h265-archive","webm","mp3","wav"],required=True)
    mn=m_sub.add_parser("normalize-audio"); mn.add_argument("source",type=Path); mn.add_argument("output",type=Path); mn.add_argument("--target-lufs",type=float,default=-16.0)
    mf=m_sub.add_parser("extract-frames"); mf.add_argument("source",type=Path); mf.add_argument("output_dir",type=Path); mf.add_argument("--fps",type=float,default=1.0)
    b=sub.add_parser("blender",help="Blender headless utilities"); b_sub=b.add_subparsers(dest="action",required=True)
    ba=b_sub.add_parser("audit"); ba.add_argument("scene",type=Path)
    br=b_sub.add_parser("render"); br.add_argument("scene",type=Path); br.add_argument("output_prefix",type=Path); br.add_argument("--frame",type=int)
    args=parser.parse_args(argv)
    try:
        if args.command=="doctor": _json(_doctor()); return 0
        if args.command=="assets":
            if args.action=="ingest":
                result=assets.ingest_many(args.sources,args.library,args.recursive); _json(result); return 5 if result.get("status")=="partial_failure" else 0
            if args.action=="list": _json(assets.list_assets(args.library)); return 0
            if args.action=="duplicates": _json(assets.duplicates(args.library)); return 0
        if args.command=="identity":
            if args.action=="init": print(identity.create_profile(args.output,args.name,args.kind)); return 0
            if args.action=="prompt":
                rendered=identity.build_prompt(args.profile,args.manifest)
                if args.output: print(write_text_no_overwrite(args.output,rendered))
                else: print(rendered,end="")
                return 0
        if args.command=="quote":
            try: qty=Decimal(args.quantity)
            except InvalidOperation: raise ValueError("quantity must be a decimal number")
            result=pricing.quote(args.rate_card,args.provider,args.model,args.unit,qty); _json(result)
            return 0 if result.get("status")=="ESTIMATE_ONLY" else 3
        if args.command=="comfyui":
            if args.action=="status": result=comfyui.status(args.url,args.allow_remote)
            elif args.action=="submit": result=comfyui.submit(args.workflow,args.url,args.allow_remote)
            elif args.action=="upload": result=comfyui.upload_image(args.source,args.url,args.allow_remote)
            else: result=comfyui.wait_for_job(args.prompt_id,args.url,args.timeout,args.interval,args.allow_remote)
            _json(result); return 0 if result.get("status")!="timeout" else 4
        if args.command=="image":
            if args.action=="info": _json(image.inspect(args.source)); return 0
            if args.action=="resize":
                if not 1<=args.quality<=100: raise ValueError("quality must be between 1 and 100")
                _json(image.resize(args.source,args.output,args.width,args.height,args.fit,args.allow_upscale,args.background,args.quality)); return 0
            if args.action=="contact-sheet": _json(image.contact_sheet(args.sources,args.output,columns=args.columns)); return 0
        if args.command=="media":
            if args.action=="probe": _json(media.probe(args.source)); return 0
            if args.action=="loudness": _json(media.measure_loudness(args.source)); return 0
            if args.action=="transcode": _json(media.transcode(args.source,args.output,args.preset)); return 0
            if args.action=="normalize-audio": _json(media.normalize_audio(args.source,args.output,args.target_lufs)); return 0
            if args.action=="extract-frames": _json(media.extract_frames(args.source,args.output_dir,args.fps)); return 0
        if args.command=="blender":
            _json(blender.audit(args.scene) if args.action=="audit" else blender.render_still(args.scene,args.output_prefix,args.frame)); return 0
    except (OSError,ValueError,RuntimeError,json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}",file=sys.stderr); return 2
    return 2
