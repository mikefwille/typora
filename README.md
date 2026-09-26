<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://typora.io">Typora</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/mikefwille/typora/stargazers"><img src="https://img.shields.io/github/stars/mikefwille/typora?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/mikefwille/typora/issues"><img src="https://img.shields.io/github/issues/mikefwille/typora?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/mikefwille/typora/contributors"><img src="https://img.shields.io/github/contributors/mikefwille/typora?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

Soothing pastels for writing in Typora, with four Catppuccin flavors and visible color in headings, emphasis, links, and code.

**[Download preview ZIP](https://github.com/mikefwille/typora/releases/download/v0.1.0/catppuccin-typora.zip)** · [Install](#installation) · [Choose a flavor](#flavors) · [Troubleshooting](#troubleshooting) · [Development](DEVELOPMENT.md)

The preview release contains the installation files, sample document, and MIT license.
[Browse releases](https://github.com/mikefwille/typora/releases) or [download the latest source](https://github.com/mikefwille/typora/archive/refs/heads/main.zip).

Community port in development; not yet adopted or endorsed by the Catppuccin organization.

## Previews

<p align="center"><img src="assets/preview.webp" alt="Four Catppuccin flavors in Typora" /></p>

<details><summary>🌻 Latte</summary><img src="assets/latte.png" alt="🌻 Latte in Typora" /></details>
<details><summary>🪴 Frappé</summary><img src="assets/frappe.png" alt="🪴 Frappé in Typora" /></details>
<details><summary>🌺 Macchiato</summary><img src="assets/macchiato.png" alt="🌺 Macchiato in Typora" /></details>
<details><summary>🌿 Mocha</summary><img src="assets/mocha.png" alt="🌿 Mocha in Typora" /></details>

## Installation

1. [Download the preview ZIP](https://github.com/mikefwille/typora/releases/download/v0.1.0/catppuccin-typora.zip) and extract it.
2. In Typora, open **Preferences → Appearance → Open Theme Folder**.
3. Copy the **contents** of `themes/` into that folder: all four CSS files and the entire `catppuccin` directory.
4. Restart Typora and select **Catppuccin Latte**, **Frappé**, **Macchiato**, or **Mocha** from **Themes**.

The four entry CSS files must be directly inside Typora's theme folder:

```text
Typora theme folder/
├── catppuccin-latte.css
├── catppuccin-frappe.css
├── catppuccin-macchiato.css
├── catppuccin-mocha.css
└── catppuccin/
    ├── base.css
    ├── accents.css
    └── latte.css, frappe.css, macchiato.css, mocha.css
```

Installing the complete `themes/` directory as a nested folder will prevent Typora from finding the entry files.
Keep the `catppuccin` directory even if you only use one flavor.
No font installation or build step is required.

### Updating or removing

To update, replace the four entry CSS files and the shared `catppuccin` directory with the new copies, then restart Typora.
Back up any personal changes before replacing them.
To remove this port, select another theme, then remove these four files and their shared directory.
Remove the optional darker Macchiato entry too if you installed it.

## Flavors

| Flavor | Appearance | Base background |
| --- | --- | --- |
| 🌻 Latte | Light | `#eff1f5` |
| 🪴 Frappé | Dark, with gray tones | `#303446` |
| 🌺 Macchiato | Dark, with blue tones | `#24273a` |
| 🌿 Mocha | Deepest standard dark flavor | `#1e1e2e` |

All four use the [official Catppuccin palette](https://catppuccin.com/palette/).
Start with Latte for a light theme or Mocha for the darkest standard background.

## Features

- Four standard Catppuccin palettes with their original backgrounds and accents.
- Pastel heading hierarchy, sapphire bold text, green italics, and rosewater quotes.
- Shared styling for the editor, sidebar, tables, code blocks, and syntax highlighting.
- System fonts; no external fonts or network requests required by the theme.

### Optional darker Macchiato

Copy [extras/catppuccin-macchiato-dark.css](extras/catppuccin-macchiato-dark.css) into your theme folder alongside the standard themes, then restart Typora and choose **Catppuccin Macchiato Dark**.
This custom blend uses Mocha backgrounds and surfaces with Macchiato text and accents.
It is a separately named customization of the palette.
Its darkness matches Mocha, and its accent differences are subtle.
The four standard themes retain their original palettes.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Theme is missing from the menu | Put the entry CSS files directly in the theme folder, then fully restart Typora. |
| Colors or layout are missing | Copy the whole shared `catppuccin` directory; each entry imports files from it. |
| An update looks unchanged | Replace both the entry files and the shared directory, then restart Typora. |
| Colors differ from the screenshots | Check [Typora's custom CSS files](https://support.typora.io/Add-Custom-CSS/) for overrides and confirm which flavor is selected. |
| Macchiato looks as dark as Mocha | Select standard Macchiato; the optional Macchiato Dark blend intentionally uses Mocha backgrounds. |

If the problem persists, [report a bug](https://github.com/mikefwille/typora/issues/new) with your Typora version, operating system, flavor, a small Markdown example, and a screenshot.

## Compatibility

The four standard flavors were visually checked in **Typora 1.14.10 on macOS 27.0** with the [preview document](examples/preview.md).

| Area | Verification |
| --- | --- |
| Headings, emphasis, links, quotes, lists, tasks, tables, Python code | Visually checked in all four standard flavors on macOS |
| Windows and Linux | Not tested |
| Dialogs, search, source mode, math, diagrams, print and export | Broader checks pending |
| Optional Macchiato Dark | Custom palette blend; separate full coverage check pending |

System fonts vary by operating system, so text metrics may differ from the previews.
See [DEVELOPMENT.md](DEVELOPMENT.md) for the verification checklist and local packaging command.

## Attribution

This port builds on [Stephan Lamoureux's Typora theme](https://github.com/stephanlamoureux/typora-catppuccin), under the MIT license.
Visible accent styling was developed by Mike Wille.
The repository structure follows [Catppuccin's template](https://github.com/catppuccin/template).

## 💝 Thanks to

- [Mike Wille](https://github.com/mikefwille)
- [Stephan Lamoureux](https://github.com/stephanlamoureux)
- [Catppuccin community](https://github.com/catppuccin)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8" alt="MIT license"/></a>
</p>
