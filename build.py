import fontforge as ff
import json
import os
import re

PATH = os.getcwd()

def load_json_with_comments(json_string, *args):
    """Load JSON with comments.
    """
    json_string = re.sub(r"//.*$", "", json_string, flags=re.MULTILINE)
    return json.loads(json_string, *args)

def _parse_json():
    with open(PATH + "/math-table.json") as f:
        return load_json_with_comments(f.read())
MATH_TABLE = _parse_json()

def _add_math_constants(font):
    for name, value in MATH_TABLE["MathConstants"].items():
        exec("font.math." + name + " = " + str(value))

def _add_math_glyph_info(font):
    for _glyph in MATH_TABLE["MathGlyphInfo"]["extendedShapes"]:
        if str(_glyph) in font:
            font[str(_glyph)].isExtendedShape = True

def _add_math_variants(font, variants_type):
    for _glyph, _var in MATH_TABLE["MathVariants"][variants_type].items():
        glyph, var = str(_glyph), str(" ".join(_var))  # Convert unicode to raw string
        if glyph in font:
            exec("font[glyph]." + variants_type + " = var")

def _add_math_components(font, components_type):
    for _glyph, _comp in MATH_TABLE["MathVariants"][components_type].items():
        glyph = str(_glyph)
        comp = tuple(tuple([str(i["name"]), int(i["isExtender"]), int(i["startConnectorLength"]), int(i["endConnectorLength"]), int(i["fullAdvance"])])
                 for i in _comp)
        if glyph in font:
            exec("font[glyph]." + components_type + " = comp")

def main():
    font = ff.open(PATH + "/LatoMath.sfd")

    # Add MATH table
    _add_math_constants(font)
    _add_math_glyph_info(font)
    _add_math_variants(font, "verticalVariants")
    _add_math_variants(font, "horizontalVariants")
    _add_math_components(font, "verticalComponents")
    _add_math_components(font, "horizontalComponents")
        
    font.generate(PATH + "/LatoMath.otf", flags=("opentype", "round"))
    font.close()
    print("Done!")

if __name__ == "__main__":
    main()
