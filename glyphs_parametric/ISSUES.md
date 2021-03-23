# Outstanding Issues

1. Many glyphs do not have a properly formed "d" attribute or it has not been updated. Need a script to cleanly create all of these. Could be useful to have this as part of the glyph registration procedure as all "d" elements should be automatically generated and not given manually.

2. Need to agree on path naming and ensuring we minimise paths to simplify customisation in tools. For example, multiple paths at present are used for wiggly location stems – need to consolidate.

3. The origin (baseline start point) is (0,0) in all glyphs. This causes them to be cropped when viewed in a Web browser or imported into Powerpoint. Could we set up clipping planes to be automatically added such that only the glyph is visible or generate shifted versions without all the bounding box and baseline? Use viewBox and remove width and height for the SVG? See SingleStrandedNuclicAcid.svg for an example

4. We should agree on the formatting of the SVG files (this could make management easier longer term). This is in terms of the text within the files (e.g. spaces for indents, ordering of attributes, etc.)

5. "Complex" is not a glyph. It is a composition of glyphs. Could these be automatically generated? It is very much a special case. Similar to how a primer binding site might be overlaid on other sequence features.

6. "No Glyph Assigned" & "Unspecified" – these already exists as sequence features. Should they just be copied? Should we have glyphs defined in two places?

7. ssNA and dsNA should be able to be concatenated to create longer versions of the symbol. A small 2 element part should be provided as symbol ensuring proper alignment of baselines will case correct joining of symbols. See ssNA for an example where this works.