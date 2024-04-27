## ---------------------------------------------------------------------------##
# Author: Beatrix Haddock
# Date: 04/26/2024
# Purpose:  Compile md to html
# INPUTS:   - md
# OUTPUTS:  - html
## ---------------------------------------------------------------------------##
import markdown
import sys

MD_FILE = sys.argv[1]

def regen_README():
    name = md_path.split("/")[-1].split(".")[0]
    with open(MD_FILE, 'r') as f:
        md_text = f.read()

    html = markdown.markdown(md_text)
    html = "<style>\n*{font-family: sans-serif;}\n</style>\n" + html

    with open(OUTPUT_DIR + name + ".html", 'w') as f:
        f.write(html)
