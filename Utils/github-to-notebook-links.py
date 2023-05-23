'''
This program takes an ipynb GitHub link and creates the corresponding Callysto, Colab, and NBViewer links.

It does this by replacing parts of the GitHub link with the appropriate domains for the other sites.

It then prints the Callysto, Colab, and NBViewer links, as well as a markdown format that can be used to 
embed them in a document. 

Run this utility directly in Colab here:

https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing
'''

def callysto(url):
    res = url.split("/")
    site = res[2]
    user = res[3]
    repo = res[4]
    treeBlob = res[5]
    branch = res[6]
    nbgitputllerUrl = "https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo="
    if site == "github.com":
        if treeBlob:
            subPath = url[url.index(branch) + len(branch) + 1:]
            nbgitputllerUrl += ("https://github.com/" + user + "/") + repo + "&branch=" + branch + "&subPath=" + subPath + "&depth=1"
        else:
            nbgitputllerUrl += url
    return nbgitputllerUrl

print('This program takes an ipynb GitHUb link and creates the corresponding NBViewer and Colab links.\n')

# Get the GitHub link of the ipynb file from the user
github_link = input('Enter the GitHub link of the ipynb file: ')

# Create the Colab link by replacing 'github' with 'githubtocolab'
colab_link = github_link.replace('github', 'githubtocolab')
# Create the NBViewer link by replacing 'github.com/' with 'nbviewer.org/github/'
nbviewer_link = github_link.replace('github.com/', 'nbviewer.org/github/')
# Create the Callysto link using the function above
callysto_link = callysto(github_link)

# Print the Colab and NBViewer links
print('Callysto')
print(callysto_link)
print('Colab')
print(colab_link)
print('NBViewer')
print(nbviewer_link)


# Print the Markdown header
print('\nMarkdown:\n')

# Print the markdown format that can be used to embed the links
print(f'[Callysto]({callysto_link}) | [Colab]({colab_link}) | [NBViewer]({nbviewer_link})')
