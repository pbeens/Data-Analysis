import nbformat
from nbformat.v4.nbbase import new_markdown_cell
import sys

# location of the Markdown file
if len(sys.argv) > 1:
    jupyter_filename = sys.argv[1]
else:
    jupyter_filename = r'D:\My Documents\GitHub\Data-Analysis\Demos\where-can-we-get-data-from copy.ipynb'

def create_toc(nb):
    toc = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown' and cell.source.startswith('#'):
            lines = cell.source.split('\n')
            level = len(lines[0].split()[0])
            title = ' '.join(lines[0].split()[1:]) if len(lines[0].split()) > 1 else ''
            toc.append((level, title))
    toc_md = ''
    for level, title in toc:
        toc_md += '  ' * (level - 1) + '- [' + title.replace('`', '') + '](#' + '-'.join(title.lower().split()).replace('`', '') + ')\n'
    return toc_md

# Read the Jupyter notebook file
with open(jupyter_filename, 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Create table of contents (TOC) Markdown
toc_md = create_toc(nb)

# Print the table of contents Markdown
print('# Table of Contents\n')
print(toc_md)
