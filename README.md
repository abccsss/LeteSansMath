# Lato Math

__Lato Math__ is a sans-serif math font,
based on the
[Lato](https://github.com/latofonts/lato-source) font.
Some of the glyphs and source files are adapted from
[XITS](https://github.com/alif-type/xits),
[STIX Two](https://www.stixfonts.org/), and
[Fira Math](https://github.com/firamath/firamath).

![Lato Math](https://www.bananaspace.net/uploads/28423489/4dc906f2b646415cbcc4955429f374e7.png)

## To build

1. Install FontForge.
2. Run `ffpython build.py`.

This will generate a file `LatoMath.otf` in the project root directory.

## To use with LaTeX

1. Copy `LatoMath.otf` to your LaTeX project directory.
2. Add the following lines to the preamble.
    ```latex
    \usepackage{unicode-math}
    \setmathfont{[LatoMath.otf]}
    ```
3. Build with `xelatex`.

## Glyph coverage

* Latin letters: roman, italic, bold, bold italic, double-struck, monospace.

* Greek letters: roman, italic, bold, bold italic.

* Digits: roman, bold, double-struck, monospace.

* All commonly used mathematical symbols.
