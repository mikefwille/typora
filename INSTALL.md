# Install Catppuccin for Typora

1. Extract the downloaded ZIP.
2. Open Typora's **Preferences → Appearance → Open Theme Folder**.
3. Copy the contents of `themes/` into that folder: four `catppuccin-*.css` files and the complete shared `catppuccin` directory.
4. Restart Typora and select a Catppuccin flavor from **Themes**.

The entry CSS files must be directly in Typora's theme folder.
Do not copy `themes/` as a nested directory.
No font installation or build step is required.

Latte is light; Frappé, Macchiato, and Mocha are dark.
Mocha has the darkest standard background.
For the optional custom blend, also copy `extras/catppuccin-macchiato-dark.css` directly into the theme folder and restart Typora.
This blend uses Mocha backgrounds with Macchiato text and accents.

For updates, replace the four entry files and their shared directory, then restart Typora.
Back up any personal modifications first.

The four standard flavors have been visually checked on macOS with the included preview document.
Windows, Linux, and broader dialog, math, diagram, and export coverage remain unverified.

[Full instructions, screenshots, compatibility, and credits](https://github.com/mikefwille/typora)

Based on Stephan Lamoureux's MIT-licensed Typora Catppuccin theme.
See `LICENSE` for the preserved license notice.
