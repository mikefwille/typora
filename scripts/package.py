#!/usr/bin/env python3
"""Build a local installation ZIP without publishing anything."""

import hashlib
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
FLAVORS = ("latte", "frappe", "macchiato", "mocha")
IMPORT = re.compile(r"@import\s+url\(\s*['\"]([^'\"]+)['\"]\s*\)\s*;")


def package():
    # Explicit inventory keeps unrelated local material out of the release.
    names = [f"themes/catppuccin-{flavor}.css" for flavor in FLAVORS]
    names += [f"themes/catppuccin/{flavor}.css" for flavor in FLAVORS]
    names += [
        "themes/catppuccin/base.css",
        "themes/catppuccin/accents.css",
        "extras/catppuccin-macchiato-dark.css",
        "INSTALL.md",
        "LICENSE",
    ]
    payload = {}
    for name in names:
        source = ROOT / name
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"Missing or symlinked package file: {name}")
        payload[name] = source.read_bytes()

    # Extras are copied beside the entry CSS when installed.
    installed = {}
    for name, content in payload.items():
        if name.endswith(".css"):
            installed[PurePosixPath(name).relative_to(name.split("/")[0])] = content
    for name, content in installed.items():
        for target in IMPORT.findall(content.decode("utf-8")):
            if ":" in target or target.startswith("/") or ".." in PurePosixPath(target).parts:
                raise ValueError(f"Import must stay inside the theme folder: {name}: {target}")
            resolved = name.parent / target
            if resolved not in installed:
                raise ValueError(f"Missing installed import: {name}: {target}")

    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / "catppuccin-typora.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for name in sorted(payload):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, payload[name])
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"Validated {len(installed)} stylesheets and their installed imports.")
    print(f"Built {archive} ({len(payload)} files)")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    try:
        package()
    except (OSError, UnicodeError, ValueError, zipfile.BadZipFile) as error:
        raise SystemExit(f"Package failed: {error}") from error
