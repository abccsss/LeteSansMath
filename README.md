# Lato Math

__Lato Math__ is an OpenType sans-serif math font,
based on the
[Lato](https://github.com/latofonts/lato-source) font.

![Lato Math](https://github.com/abccsss/LatoMath/assets/23280392/49a23583-f63c-45ba-83cd-ec4cdfc6d1a1)

This repository contains the content of the LaTeX package `lato-math`,
including OpenType font files, LaTeX style files, and documentation.
You can also view the package on
[CTAN](https://ctan.org/pkg/lato-math).

## Contents

* `LatoMath.otf`
	— The OpenType font file.
* `LatoMath-Bold.otf`
	— The OpenType font file for the bold variant (limited coverage).
* `lato-math.sty`
	— The LaTeX style file.
* `LatoMath.pdf`
	— Documentation of the package.
* `LatoMath.ltx`
	— The LaTeX source of `LatoMath.pdf`.
* `unimath-lato.pdf`
	— A modified version of `unimath-symbols.pdf`
	from the `unicode-math` package,
	showing available Lato Math symbols compared
	to other sans-serif math fonts.
* `unimath-lato.ltx`
	— The LaTeX source of `unimath-lato.pdf`.

## Usage

This package is meant to be installed automatically by TeX Live, MikTeX, etc. Use
```latex
\usepackage{lato-math}
```
to load the package.
The package requires XeLaTeX or LuaLaTeX to compile.
For more information such as package options,
see the documentation `LatoMath.pdf`.

To load the package manually, place the files
`lato-math.sty`, `LatoMath.otf`, and `LatoMath-Bold.otf`
in your project directory,
and use the same call as above.

It is also possible to use the font without the `lato-math` package.
See the documentation `LatoMath.pdf` for details.

## Changes

### v0.37 (2024-04-18)

* Glyphs U+2234–U+223B and sans-serif Greek letters U+1D756–U+1D7CB added to the bold variant.

### v0.36 (2024-03-14)

* First public release.
