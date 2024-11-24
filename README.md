# Lete Sans Math

**Authors:** Chenjing Bu and Daniel Flipo

**Lete Sans Math** is an OpenType sans-serif math font,
based on the
[Lato](https://github.com/latofonts/lato-source) font.

![Lete Sans Math](https://github.com/abccsss/LeteSansMath/assets/23280392/49a23583-f63c-45ba-83cd-ec4cdfc6d1a1)

This repository contains the content of the LaTeX package `lete-sans-math`,
including OpenType font files, LaTeX style files, and documentation.
You can also view the package on
[CTAN](https://ctan.org/pkg/lete-sans-math).

## Contents

- `LeteSansMath.otf`
  — The OpenType font file.
- `LeteSansMath-Bold.otf`
  — The OpenType font file for the bold variant (limited coverage).
- `lete-sans-math.sty`
  — The LaTeX style file.
- `LeteSansMath.pdf`
  — Documentation of the package.
- `LeteSansMath.ltx`
  — The LaTeX source of `LeteSansMath.pdf`.
- `unimath-lete.pdf`
  — A modified version of `unimath-symbols.pdf`
  from the `unicode-math` package,
  showing available Lete Sans Math symbols compared
  to other sans-serif math fonts.
- `unimath-lete.ltx`
  — The LaTeX source of `unimath-lete.pdf`.

## Usage

This package is meant to be installed automatically by TeX Live, MikTeX, etc. Use

```latex
\usepackage{lete-sans-math}
```

to load the package.
The package requires XeLaTeX or LuaLaTeX to compile.
For more information such as package options,
see the documentation `LeteSansMath.pdf`.

To load the package manually, place the files
`lete-sans-math.sty`, `LeteSansMath.otf`, and `LeteSansMath-Bold.otf`
in your project directory,
and use the same call as above.

It is also possible to use the font without the `lete-sans-math` package.
See the documentation `LeteSansMath.pdf` for details.

## License

- The font files `LeteSansMath.otf` and `LeteSansMath-Bold.otf`
  are licensed under the
  [SIL Open Font License (OFL) Version 1.1](http://scripts.sil.org/OFL).

- The other files are distributed under the terms of the
  [LaTeX Project Public License (LPPL) Version 1.3c](https://ctan.org/tex-archive/macros/latex/base/lppl.txt).

## Changes

### v0.44 (2024-11-24)

- Triple and quadruple stroked arrows (U+21DA, U+21DB, U+2B45, U+2B46)
  are extensible again.

### v0.43 (2024-11-23)

- Glyphs U+0332 and U+23DC to U+23DF resized for consistency.
- Fixed vertical composition of int symbol (U+222B).
- Glyphs U+21D0 to U+21D5, U+27F8 to U+27FA, U+27FD, and U+27FE
  slightly changed to be constent with the equal sign (U+003D).
  Horizontal composition of these arrows reworked.

### v0.41 (2024-07-18)

- Added feature `cv11` to provide a single-storey variant for the lowercase letter g.

### v0.40 (2024-05-12)

- Rename the font as 'Lete Sans Math' due to copyright reasons.

### v0.37 (2024-04-18)

- Glyphs U+2234–U+223B and sans-serif Greek letters U+1D756–U+1D7CB added to the bold variant.

### v0.36 (2024-03-14)

- First public release.
