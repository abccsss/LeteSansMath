# Lete Sans Math

__Lete Sans Math__ is an OpenType sans-serif math font,
based on the
[Lato](https://github.com/latofonts/lato-source) font.

![Lete Sans Math](https://github.com/abccsss/LeteSansMath/assets/23280392/49a23583-f63c-45ba-83cd-ec4cdfc6d1a1)

This repository contains the content of the LaTeX package `lete-sans-math`,
including OpenType font files, LaTeX style files, and documentation.
You can also view the package on
[CTAN](https://ctan.org/pkg/lete-sans-math).

## Contents

* `LeteSansMath.otf`
	— The OpenType font file.
* `LeteSansMath-Bold.otf`
	— The OpenType font file for the bold variant (limited coverage).
* `lete-sans-math.sty`
	— The LaTeX style file.
* `LeteSansMath.pdf`
	— Documentation of the package.
* `LeteSansMath.ltx`
	— The LaTeX source of `LeteSansMath.pdf`.
* `unimath-lete.pdf`
	— A modified version of `unimath-symbols.pdf`
	from the `unicode-math` package,
	showing available Lete Sans Math symbols compared
	to other sans-serif math fonts.
* `unimath-lete.ltx`
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

## Changes

### v0.40 (2024-05-12)

* Rename the font as 'Lete Sans Math' due to copyright reasons.

### v0.37 (2024-04-18)

* Glyphs U+2234–U+223B and sans-serif Greek letters U+1D756–U+1D7CB added to the bold variant.

### v0.36 (2024-03-14)

* First public release.
