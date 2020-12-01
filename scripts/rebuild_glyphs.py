import json
import os

script_path = os.path.realpath(__file__)
script_dir = os.path.abspath(os.path.join(script_path, os.pardir))

cmd_path = os.path.abspath(os.path.join(script_dir, os.pardir, "node_modules", "markdown-pdf", "bin", "markdown-pdf"))

with open(os.path.join(script_dir, "glyph_list.json")) as fp:
    data = json.load(fp)


definitions_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

initial_path = os.getcwd()

version_macros = {
    "2.1.0": "\\twoonezeronopage",
    "2.2.0": "\\twotwozeronopage",
    "2.3.0": "\\twothreezeronopage"
}

for glyph_category in data:

    # Generate individual PDF files for each glyph
    for glyph in glyph_category["glyphs"]:
        glyph_name = glyph["name"]

        readme_dir = os.path.join(definitions_dir, 'Glyphs', glyph_category["dir"], glyph_name)
        readme_file = os.path.join(readme_dir, "README.md")

        # absolute path to output PDF
        pdf_name = os.path.abspath(os.path.join(script_dir, os.path.pardir, "specification", "glyphscript", "Glyphs", glyph_category["dir"], glyph_name + ".pdf"))

        if os.path.exists(readme_file):

            # Skip PDF generation if PDF has been modified more recently than the dir containing README & image files
            if os.path.exists(pdf_name) and os.path.getmtime(pdf_name) > os.path.getmtime(readme_dir):
                continue

            # We need to change directory so that the relative paths to images used in README.md work correctly
            os.chdir(readme_dir)
            os.system(f"{cmd_path} README.md --out {pdf_name}")
        else:
            print("Missing README file:", readme_file)

    # Generate .tex file including all glyphs for each category
    glyph_category_file = os.path.abspath(os.path.join(script_dir, os.path.pardir, "specification", "glyphscript", glyph_category["output"]))
    with open(glyph_category_file, "w") as output_file:
        output_file.write("% Autogenerated glyph page collection, do not edit by hand\n")

        for glyph in glyph_category["glyphs"]:
            glyph_name = glyph["name"]

            if glyph["lastEdited"]:
                output_file.write(version_macros[glyph["lastEdited"]] + "{\n")

            relative_pdf_path = os.path.join("glyphscript", "Glyphs", glyph_category["dir"], glyph_name + ".pdf")
            output_file.write("\\includepdf[pagecommand={},pages={1-}]{%s}\n" % relative_pdf_path)

            if glyph["lastEdited"]:
                output_file.write("}\n")
