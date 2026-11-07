from __future__ import annotations
import json, tempfile, unittest
from unittest.mock import Mock
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from agentic_skill_garage.assets import ingest, ingest_many, list_assets
from agentic_skill_garage.identity import create_profile, build_prompt
from agentic_skill_garage.pricing import quote
from agentic_skill_garage.security import validate_local_url
from agentic_skill_garage import media, image, comfyui

class AssetTests(unittest.TestCase):
    def test_ingest_hashes_and_copies(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"src.bin"; src.write_bytes(b"abc")
            result=ingest(src,root/"library")
            self.assertEqual(result["status"],"ingested")
            self.assertEqual((root/"library"/"src.bin").read_bytes(),b"abc")
            self.assertEqual(len(list_assets(root/"library")),1)
    def test_duplicate_by_hash_not_filename(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); a=root/"a.png"; b=root/"b.png"; a.write_bytes(b"same"); b.write_bytes(b"same")
            ingest(a,root/"lib"); result=ingest(b,root/"lib")
            self.assertEqual(result["status"],"duplicate")
    def test_manifest_rejects_non_object_json(self):
        with tempfile.TemporaryDirectory() as d:
            library=Path(d)/"library"; library.mkdir()
            (library/"manifest.jsonl").write_text("[]\n",encoding="utf-8")
            with self.assertRaises(ValueError):
                list_assets(library)
    def test_existing_destination_never_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"src"; src.write_text("new")
            lib=root/"lib"; lib.mkdir(); (lib/"src").write_text("keep")
            with self.assertRaises(FileExistsError): ingest(src,lib)
            self.assertEqual((lib/"src").read_text(),"keep")
    def test_recursive_batch_ingest_preserves_folder_paths_and_skips_hidden(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); refs=root/"references"; (refs/"characters").mkdir(parents=True)
            (refs/"characters"/"hero.png").write_bytes(b"hero")
            (refs/".private").write_text("do not copy")
            (refs/".cache").mkdir(); (refs/".cache"/"hidden.bin").write_bytes(b"skip")
            result=ingest_many([refs],root/"library",recursive=True)
            self.assertEqual(result["ingested"],1)
            self.assertTrue((root/"library"/"references"/"characters"/"hero.png").exists())
            self.assertFalse((root/"library"/".private").exists())
    def test_directory_input_requires_recursive_opt_in(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); folder=root/"refs"; folder.mkdir(); (folder/"a.png").write_bytes(b"a")
            with self.assertRaises(ValueError): ingest_many([folder],root/"library")
    def test_manifest_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"src"; src.write_text("x")
            outside=root/"outside"; outside.write_text("do not append")
            lib=root/"lib"; lib.mkdir(); (lib/"manifest.jsonl").symlink_to(outside)
            with self.assertRaises(ValueError): ingest(src,lib)
            self.assertEqual(outside.read_text(),"do not append")
    def test_symlink_input_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"src"; src.write_text("x"); link=root/"link"; link.symlink_to(src)
            with self.assertRaises(ValueError): ingest(link,root/"lib")

class IdentityTests(unittest.TestCase):
    def test_profile_prompt_includes_invariants(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"identity.json"; create_profile(p,"Nova")
            data=json.loads(p.read_text()); data["canonical_description"]="Silver jacket, short hair."; data["invariants"]=["Keep the silver jacket."]
            p.write_text(json.dumps(data))
            prompt=build_prompt(p)
            self.assertIn("Keep the silver jacket",prompt)
    def test_profile_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"identity.json"; p.write_text("keep")
            with self.assertRaises(FileExistsError): create_profile(p,"Nova")

class PricingTests(unittest.TestCase):
    def test_missing_price_is_unpriced(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"rates.json"; p.write_text(json.dumps({"rates":[]}))
            self.assertEqual(quote(p,"p","m","image",Decimal("2"))["status"],"UNPRICED")
    def test_non_finite_quantity_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"rates.json"; p.write_text(json.dumps({"rates":[]}))
            self.assertEqual(quote(p,"p","m","image",Decimal("NaN"))["status"],"INVALID_QUANTITY")
    def test_unverified_rate_is_not_quoted(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"rates.json"; p.write_text(json.dumps({"rates":[{"provider":"p","model":"m","unit":"image","price_per_unit":"0.1"}]}))
            self.assertEqual(quote(p,"p","m","image",Decimal("2"))["status"],"UNVERIFIED")

class SafetyTests(unittest.TestCase):
    def test_loopback_allowed(self): self.assertEqual(validate_local_url("http://127.0.0.1:8188"),"http://127.0.0.1:8188")
    def test_remote_rejected_without_opt_in(self):
        with self.assertRaises(ValueError): validate_local_url("https://example.com")
    def test_remote_can_be_explicitly_allowed(self): self.assertTrue(validate_local_url("https://example.com",True).startswith("https://"))
    def test_remote_http_is_never_allowed(self):
        with self.assertRaises(ValueError): validate_local_url("http://example.com",True)
    def test_endpoint_query_cannot_carry_credentials(self):
        with self.assertRaises(ValueError): validate_local_url("https://example.com?token=secret",True)

class ComfyUITests(unittest.TestCase):
    def test_upload_sends_explicit_file_to_local_upload_endpoint(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"reference image.png"; src.write_bytes(b"image-bytes")
            response=Mock(); response.read.return_value=b'{"name":"reference_image.png","type":"input"}'
            response.__enter__=Mock(return_value=response); response.__exit__=Mock(return_value=False)
            opener=Mock(); opener.open.return_value=response
            with patch("agentic_skill_garage.comfyui.urllib.request.build_opener",return_value=opener) as build:
                result=comfyui.upload_image(src,"http://127.0.0.1:8188")
            build.assert_called_once_with(comfyui._NoRedirect)
            req=opener.open.call_args.args[0]
            self.assertEqual(req.full_url,"http://127.0.0.1:8188/upload/image")
            self.assertIn(b"image-bytes",req.data)
            self.assertEqual(result["bytes"],11)
    def test_upload_remote_requires_explicit_remote_flag_and_https(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"ref.png"; src.write_bytes(b"x")
            with self.assertRaises(ValueError): comfyui.upload_image(src,"http://example.com")
    def test_wait_polls_until_job_is_complete(self):
        pid="a"*32
        with patch.object(comfyui,"request",side_effect=[{}, {pid:{"status":{"completed":True,"status_str":"success"}}}]) as req, patch.object(comfyui.time,"sleep"):
            result=comfyui.wait_for_job(pid,"http://127.0.0.1:8188",timeout=5,interval=0.25)
        self.assertEqual(result["status"],"completed")
        self.assertEqual(req.call_count,2)
    def test_wait_rejects_untrusted_prompt_ids(self):
        with self.assertRaises(ValueError): comfyui.wait_for_job("../../etc/passwd","http://127.0.0.1:8188")

class ImageTests(unittest.TestCase):
    def test_resize_creates_exact_canvas_and_never_overwrites(self):
        try: from PIL import Image
        except ImportError: self.skipTest("Pillow unavailable")
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.png"; Image.new("RGB",(100,50),(255,0,0)).save(src)
            out=root/"out.png"
            result=image.resize(src,out,200,100,fit="contain",allow_upscale=True)
            self.assertEqual((result["width"],result["height"]),(200,100))
            with self.assertRaises(FileExistsError): image.resize(src,out,200,100,fit="contain",allow_upscale=True)
    def test_resize_strips_exif_metadata(self):
        try: from PIL import Image
        except ImportError: self.skipTest("Pillow unavailable")
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"with-private-metadata.png"; out=root/"clean.png"
            original=Image.new("RGB",(100,100),(20,40,60))
            exif=Image.Exif(); exif[315]="Private author name"
            original.save(src,exif=exif)
            image.resize(src,out,100,100,fit="contain")
            with Image.open(out) as rendered:
                self.assertNotIn(315,rendered.getexif())
                self.assertNotIn("exif",rendered.info)

    def test_contact_sheet_rejects_empty_input(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): image.contact_sheet([],Path(d)/"sheet.png")
    def test_resize_rejects_symlink_output_path(self):
        try: from PIL import Image
        except ImportError: self.skipTest("Pillow unavailable")
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.png"; Image.new("RGB",(100,50)).save(src)
            elsewhere=root/"elsewhere.png"; elsewhere.write_bytes(b"keep")
            link=root/"out.png"; link.symlink_to(elsewhere)
            with self.assertRaises(ValueError): image.resize(src,link,100,50)
            self.assertEqual(elsewhere.read_bytes(),b"keep")

class MediaTests(unittest.TestCase):
    def test_transcode_failure_preserves_destination_created_during_run(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.mov"; src.write_bytes(b"source")
            output=root/"out.mp4"
            def fail_after_concurrent_create(command,**kwargs):
                Path(command[-1]).write_bytes(b"partial staged output")
                output.write_bytes(b"user-created file")
                return Mock(returncode=1,stderr="simulated ffmpeg failure")
            with patch("agentic_skill_garage.media._binary",return_value="ffmpeg"), \
                 patch("agentic_skill_garage.media.subprocess.run",side_effect=fail_after_concurrent_create):
                with self.assertRaises(RuntimeError):
                    media.transcode(src,output,"h264-web")
            self.assertEqual(output.read_bytes(),b"user-created file")

    def test_extract_frames_failure_does_not_delete_user_frame(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.mov"; src.write_bytes(b"source")
            output=root/"frames"
            user_frame=output/"frame-000001.jpg"
            def fail_after_concurrent_create(command,**kwargs):
                output.mkdir()
                user_frame.write_bytes(b"user-frame")
                staged_pattern=Path(command[-1])
                (staged_pattern.parent/"frame-000001.jpg").write_bytes(b"partial staged frame")
                return Mock(returncode=1,stderr="simulated ffmpeg failure")
            with patch("agentic_skill_garage.media._binary",return_value="ffmpeg"), \
                 patch("agentic_skill_garage.media.subprocess.run",side_effect=fail_after_concurrent_create):
                with self.assertRaises(RuntimeError):
                    media.extract_frames(src,output,1.0)
            self.assertEqual(user_frame.read_bytes(),b"user-frame")

    def test_transcode_preset_is_allowlisted(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.mov"; src.write_bytes(b"x")
            with self.assertRaises(ValueError): media.transcode(src,Path(d)/"out.mp4","invalid")
    def test_output_must_differ_from_source(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"same.bin"; src.write_bytes(b"x")
            with self.assertRaises(ValueError): media._output_path(src,src)
    def test_loudness_parser_returns_measured_values(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.wav"; src.write_bytes(b"x")
            stderr="""Summary:\n  Integrated loudness:\n    I:         -16.2 LUFS\n  Loudness range:\n    LRA:        3.4 LU\n  True peak:\n    Peak:      -1.3 dBFS\n"""
            result=Mock(returncode=0,stderr=stderr,stdout="")
            with patch("agentic_skill_garage.media._binary",return_value="ffmpeg"), \
                 patch("agentic_skill_garage.media.subprocess.run",return_value=result):
                measured=media.measure_loudness(src)
            self.assertEqual(measured["status"],"measured")
            self.assertEqual(measured["integrated_lufs"],-16.2)
            self.assertEqual(measured["true_peak_dbfs"],-1.3)
    def test_non_finite_media_parameters_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.wav"; src.write_bytes(b"x")
            with self.assertRaises(ValueError): media.normalize_audio(src,Path(d)/"out.wav",float("nan"))
            with self.assertRaises(ValueError): media.extract_frames(src,Path(d)/"frames",float("nan"))
    def test_symlink_output_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.mov"; src.write_bytes(b"x")
            elsewhere=root/"elsewhere"; elsewhere.mkdir()
            link=root/"linked"; link.symlink_to(elsewhere, target_is_directory=True)
            with self.assertRaises(ValueError): media._output_path(src,link/"out.mp4")
    def test_extract_frames_rejects_symlink_output_directory(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"in.mov"; src.write_bytes(b"x")
            elsewhere=root/"elsewhere"; elsewhere.mkdir()
            link=root/"linked"; link.symlink_to(elsewhere, target_is_directory=True)
            with self.assertRaises(ValueError): media.extract_frames(src,link,1.0)

if __name__=="__main__": unittest.main()
