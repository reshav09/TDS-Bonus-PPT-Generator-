# app/utils.py
import os, re, time
from typing import Optional

SAFE_CHARS = re.compile(r"[^A-Za-z0-9._-]+")


def safe_filename(name: str, default: str = "slides") -> str:
    name = name.strip() or default
    name = SAFE_CHARS.sub("-", name)
    return name[:80]


def tmp_path(basename: str, ext: str) -> str:
    ts = int(time.time()*1000)
    return f"/tmp/{basename}-{ts}.{ext.lstrip('.')}"