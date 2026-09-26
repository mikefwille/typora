# Development and verification

Bug reports and focused fixes are welcome.
This is a community port in development; adoption by Catppuccin has not yet been requested.

## Report a problem

Include the Typora version, operating system, exact flavor, reproduction steps, a small Markdown example, and a screenshot.
Mention any custom CSS or Typora plugins that may affect the result.
Use sample content you can share publicly.

## Theme structure

| Path | Purpose |
| --- | --- |
| `themes/catppuccin-*.css` | Four selectable standard theme entries |
| `themes/catppuccin/base.css` | Shared Typora layout, interface and code styles |
| `themes/catppuccin/{latte,frappe,macchiato,mocha}.css` | Standard palette variables |
| `themes/catppuccin/accents.css` | Shared pastel Markdown accents and font choices |
| `extras/` | Explicitly named palette customizations |
| `examples/preview.md` | Sample used for the screenshots |
| `assets/` | Actual Typora screenshots and the Catwalk overview |

Keep standard palettes aligned with the [official palette](https://catppuccin.com/palette/).
Use semantic palette variables for shared styles and [Typora's theme variables](https://theme.typora.io/doc/Write-Custom-Theme/) for its interface.
Refer to [Catppuccin's style guide](https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md) when choosing colors.
Keep custom blends separately named so the standard flavor names remain predictable.
Preserve upstream credits and MIT notices.

No stylesheet compilation or external font download is required.
Copy the contents of `themes/` into Typora's theme folder and restart the app to test changes.

## Verify a change

Reproduce the reported problem in Typora before changing CSS.
Check the changed component in Latte, Frappé, Macchiato, and Mocha.
Use `examples/preview.md` for the baseline and a small additional example for the affected feature.

- Check headings, emphasis, links, inline code, code fences, quotes, lists, tasks and tables.
- Check the file sidebar, outline, search, selection and source mode when interface styles change.
- Check math and Mermaid diagrams when their styles change.
- Check PDF/HTML export and print preview when document layout changes.
- Record the Typora version and operating system actually used.
- Disclose platforms and features you did not verify.

The current baseline is a visual check of the preview document in all four standard flavors on Typora 1.14.10 / macOS 27.0.
Windows, Linux, dialogs, source mode, search, math, diagrams and print/export still need broader coverage.
Packaging validation checks file integrity and imports; it does not verify visual rendering.

## Build a local release ZIP

With Python 3.9 or newer, run from the repository root:

```sh
python3 scripts/package.py
```

This writes `dist/catppuccin-typora.zip` and a SHA-256 checksum alongside it.
The ZIP includes `themes/`, `extras/`, `INSTALL.md` and `LICENSE`.
It excludes local drafts, review surfaces, Git metadata, and development files.
The script checks that every CSS import resolves after installation and that all four standard entries are present.
Extract the ZIP and follow `INSTALL.md` for a final installation check.

Rebuild it after any change to the theme or installation instructions.
Publishing a release is a separate maintainer action.

## Update previews

Capture the sample document in the real Typora app using each standard flavor.
Keep the document, window dimensions and zoom consistent.
Save individual images under `assets/` and use [Catwalk](https://github.com/catppuccin/catwalk) to produce the four-flavor `assets/preview.webp` overview.
Update the README compatibility record if verification coverage changes.
