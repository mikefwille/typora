#!/usr/bin/env python3
"""Verify documentation links and the actual distributable, without Typora."""

import hashlib
import re
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from package import ROOT, package


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(value for key, value in attrs if key in ("href", "src") and value)


def check_docs():
    for name in ("README.md", "INSTALL.md", "DEVELOPMENT.md"):
        source = (ROOT / name).read_text(encoding="utf-8")
        parser = LocalLinks()
        parser.feed(source)
        links = parser.links + re.findall(r"\]\(([^\s)]+)\)", source)
        for link in links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (ROOT / unquote(url.path)).resolve()
            if ROOT not in path.parents or not path.is_file():
                raise ValueError(f"Broken local documentation link in {name}: {link}")
    print("Local documentation links and image paths resolve.")


def check_bundle():
    package()
    archive = ROOT / "dist/catppuccin-typora.zip"
    first_build = archive.read_bytes()
    digest = hashlib.sha256(first_build).hexdigest()
    checksum = archive.with_suffix(".zip.sha256").read_text(encoding="utf-8")
    if checksum != f"{digest}  {archive.name}\n":
        raise ValueError("Release checksum does not match the ZIP.")
    with zipfile.ZipFile(archive) as bundle, tempfile.TemporaryDirectory() as scratch:
        if bundle.testzip():
            raise ValueError("Corrupt ZIP member.")
        for name in bundle.namelist():
            path = Path(name)
            if path.is_absolute() or ".." in path.parts or path.parts[0] not in (
                "themes", "extras", "examples", "INSTALL.md", "LICENSE"
            ):
                raise ValueError(f"Unexpected release member: {name}")
            if bundle.read(name) != (ROOT / name).read_bytes():
                raise ValueError(f"Release file differs from source: {name}")
        bundle.extractall(scratch)
        installed = Path(scratch) / "themes"
        extra = Path(scratch) / "extras/catppuccin-macchiato-dark.css"
        (installed / extra.name).write_bytes(extra.read_bytes())
        if not (Path(scratch) / "examples/preview.md").is_file():
            raise ValueError("Release omits the documented sample.")
        for css in installed.rglob("*.css"):
            for target in re.findall(r"@import\s+url\(['\"]([^'\"]+)['\"]\)", css.read_text(encoding="utf-8")):
                if not (css.parent / target).is_file():
                    raise ValueError(f"Missing installed import: {css.name}: {target}")
    package()
    if archive.read_bytes() != first_build:
        raise ValueError("Repeated builds produced different ZIP bytes.")
    print("Extracted installation, sample, source bytes, checksum and repeat build pass.")


if __name__ == "__main__":
    try:
        check_docs()
        check_bundle()
    except (OSError, UnicodeError, ValueError, zipfile.BadZipFile) as error:
        raise SystemExit(f"Verification failed: {error}") from error
