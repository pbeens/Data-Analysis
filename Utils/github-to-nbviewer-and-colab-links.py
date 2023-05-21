'''
This program takes an ipynb GitHub link and creates the corresponding NBViewer and Colab links.

It does this by replacing parts of the GitHub link with the appropriate domains for NBViewer 
and Colab.

It then prints the Colab and NBViewer links, as well as a markdown format that can be used to 
embed them in a document. 

Run this utility directly in Colab here:

https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing
'''

print('This program takes an ipynb GitHUb link and creates the corresponding NBViewer and Colab links.\n')

# Get the GitHub link of the ipynb file from the user
github_link = input('Enter the GitHub link of the ipynb file: ')

# Create the Colab link by replacing 'github' with 'githubtocolab'
colab_link = github_link.replace('github', 'githubtocolab')
# Create the NBViewer link by replacing 'github.com/' with 'nbviewer.org/github/'
nbviewer_link = github_link.replace('github.com/', 'nbviewer.org/github/')

# TODO Fix Callysto link
# Create the Callysto link (NOT WORKING!)
# callysto_link = 'https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=' + github_link

# Print the Colab and NBViewer links
print('Colab')
print(colab_link)
print('NBViewer')
print(nbviewer_link)
# print('Callysto')
# print(callysto_link)

# Print the Markdown header
print('\nMarkdown:\n')

# Print the markdown format that can be used to embed the links
print(f'[Colab]({colab_link}) | [NBViewer]({nbviewer_link})')
