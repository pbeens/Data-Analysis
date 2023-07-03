import nbformat
from nbformat.v4.nbbase import new_markdown_cell
import sys

# location of the Markdown file
if len(sys.argv) > 1:
    jupyter_filename = sys.argv[1]
else:
    jupyter_filename = r'D:\My Documents\GitHub\basketball-and-data-science\content\Copies\09-machine-learning.ipynb'

def create_toc(nb):
    '''
    This code defines a function called create_toc that takes a parameter nb. It creates a table of contents (TOC) from a 
    Jupyter notebook. It iterates over each cell in the notebook and checks if it is a markdown cell starting with a 
    heading (#). If it is, it extracts the heading level and title, and adds them to the TOC list. Finally, it generates 
    and returns a markdown string representing the TOC and returns it as a new markdown cell.  
    '''
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

# Read the Jupyter notebook file
with open(jupyter_filename, 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Create table of contents (TOC) cell
toc_cell = create_toc(nb)

# Insert TOC cell at the beginning of the notebook
nb.cells.insert(0, new_markdown_cell(source='# Table of Contents\n\n'))
nb.cells.insert(1, toc_cell)

# Write the modified notebook back to the file
with open(jupyter_filename, 'w') as f:
    nbformat.write(nb, f)
