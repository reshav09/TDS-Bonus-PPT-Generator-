# app/main.py
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.background import BackgroundTask
from typing import Optional
import io, os, tempfile

from .pptx_builder import build_presentation, parse_markdown, parse_text
from .utils import safe_filename

app = FastAPI(title="Text → PowerPoint")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    with open(os.path.join(os.path.dirname(__file__), "..", "static", "index.html"), "r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)

@app.post("/generate")
async def generate(
    text: str = Form(...),
    mode: str = Form("auto"),   # auto|markdown|text
    brand_hex: Optional[str] = Form(None),
    filename: Optional[str] = Form("My Presentation"),
    template: Optional[UploadFile] = File(None),
):
    template_path = None
    try:
        if template is not None:
            ext = os.path.splitext(template.filename)[1].lower()
            if ext not in {".pptx", ".potx"}:
                return JSONResponse({"error": "Template must be .pptx or .potx"}, status_code=400)
            tmpdir = tempfile.gettempdir()
            tmp = os.path.join(tmpdir, f"uploaded{ext}")
            with open(tmp, "wb") as out:
                out.write(await template.read())
            template_path = tmp

        brand_rgb = None
        if brand_hex:
            hx = brand_hex.lstrip('#')
            if len(hx) in (3, 6):
                if len(hx) == 3:
                    hx = ''.join([c*2 for c in hx])
                brand_rgb = tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))

        prs = build_presentation(text=text, mode=mode, template_path=template_path, brand_rgb=brand_rgb)
        bio = io.BytesIO()
        prs.save(bio)
        bio.seek(0)

        fname = safe_filename(filename or "My Presentation") + ".pptx"
        return StreamingResponse(
            bio,
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            headers={"Content-Disposition": f"attachment; filename=\"{fname}\""},
            background=BackgroundTask(lambda: None)
        )
    finally:
        # Clean temp upload if present
        if template_path and os.path.exists(template_path):
            try:
                os.remove(template_path)
            except Exception:
                pass
