import nbformat
from nbformat.v4.nbbase import new_markdown_cell
import sys

# location of the Markdown file
if len(sys.argv) > 1:
    jupyter_filename = sys.argv[1]
else:
    jupyter_filename = r'D:\My Documents\GitHub\basketball-and-data-science\content\Copies\09-machine-learning.ipynb'

def create_toc(nb):
    toc = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown' and cell.source.startswith('#'):
            lines = cell.source.split('\n')
            level = len(lines[0].split()[0])
            title = ' '.join(lines[0].split()[1:]) if len(lines[0].split()) > 1 else ''
            # print(title)
            toc.append((level, title))
    toc_md = ''
    for level, title in toc:
        toc_md += '  ' * (level - 1) + '- [' + title + '](#' + '-'.join(title.lower().split()) + ')\n'
    return new_markdown_cell(source=toc_md)



with open(jupyter_filename, 'r') as f:
    nb = nbformat.read(f, as_version=4)

toc_cell = create_toc(nb)
# print(toc_cell)
nb.cells.insert(0, new_markdown_cell(source='# Table of Contents\n\n'))
nb.cells.insert(1, toc_cell)

with open(jupyter_filename, 'w') as f:
    nbformat.write(nb, f)