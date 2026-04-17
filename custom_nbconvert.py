import os
import sys
import json
from pathlib import Path
import re


ROOT = os.getcwd()

def main(nb_path: str):
    abs_nb_path = Path(ROOT) / nb_path
    fname = abs_nb_path.stem

    with open(abs_nb_path, "r") as f:
        nb = json.load(f)
    md = ""

    for cell in nb["cells"]:
        # markdown block
        if cell["cell_type"] == "markdown":
            md_cell = "".join(line for line in cell["source"])
            md_cell += "\n\n"

            # escape '|' characters, because they break mathjax
            md_cell = re.sub("[|]", r"\|", md_cell)
            md += md_cell

        # code block
        elif cell["cell_type"] == "code":
            md += "```python\n"
            md += "".join(line for line in cell["source"])
            md += "\n```\n\n"

            # handle text, image or html outputs
            for o in cell["outputs"]:
                try:
                    # handle pandas dataframes
                    if "text/html" in o["data"]:
                        md += "".join(line for line in o["data"]["text/html"])
                        md += "\n\n"
                    
                    # handle plain text
                    elif "text/plain" in o["data"]:
                        md += "```\n"
                        md += "\n".join(line for line in o["data"]["text/plain"])
                        md += "\n```\n\n"
                    
                    # handle images
                    if "image/png" in o["data"]:
                        # grab raw image byte string
                        img = o["data"]["image/png"]

                        # add image to markdown
                        md += f'<img alt="No description has been provided for this image" class="" src="data:image/png;base64,{img}"/>'
                        md += "\n\n"
                except KeyError:
                    pass

                try:
                    # handle print outputs
                    text = "".join(line for line in o["text"])
                    md += "```\n"
                    md += text
                    md += "```\n\n"
                except KeyError:
                    pass
    
    fpath = f"{ROOT}/_posts/{fname}.md"
    with open(fpath, "w") as f:
        f.write(md)
    print(f"Written to {fpath}")


if __name__ == "__main__":
    main(sys.argv[1])