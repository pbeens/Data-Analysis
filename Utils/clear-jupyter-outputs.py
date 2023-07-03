# Adapted from https://gist.github.com/misterhay/62f2dbfffd9b66288d54b25607a8717a#file-clear_jupyter_outputs-py
# Used with permission


import os
import json

# Substitute folder here
folder = r'D:\My Documents\GitHub\Data-Analysis\Demos'

def clear_outputs(notebook_name_and_path):
    """
    This function clears the outputs of a Jupyter notebook file.
    """
    # Open the original file and load its contents into a dictionary
    original_file = open(notebook_name_and_path, 'r')
    notebook_contents = json.load(original_file)
    original_file.close()

    # Iterate over each cell in the notebook
    for cell in notebook_contents['cells']:
        # Check if the cell is a code cell
        if cell['cell_type']=='code':
            # Clear the outputs and execution count of the cell
            cell['outputs'] = []
            cell['execution_count'] = None

    # Write the modified contents back to the original file
    with open(notebook_name_and_path, 'w') as notebook_file:
        json.dump(notebook_contents, notebook_file)

# Iterate over each file in the specified directory
for root, dirs, files in os.walk(folder):
    for filename in files:
        # Check if the file is a Jupyter notebook and not a checkpoint file
        if filename.endswith('.ipynb'):
            if not 'checkpoint' in filename:
                # Get the name and path of the notebook file
                notebook_name, extension = os.path.splitext(filename)
                notebook_name_and_path = os.path.join(root, filename)

                # Open the notebook file and load its contents into a dictionary
                notebook_file = open(notebook_name_and_path)
                notebook_contents = json.load(notebook_file)

                # Iterate over each cell in the notebook
                for cell in notebook_contents['cells']:
                    # Check if the cell is a code cell and has outputs
                    if cell['cell_type']=='code':
                        outputs = cell['outputs']
                        if len(outputs) > 0:
                            # If it has outputs, clear them using the clear_outputs() function
                            notebook_file.close()
                            clear_outputs(notebook_name_and_path)
