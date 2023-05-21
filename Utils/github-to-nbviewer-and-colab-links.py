print('This program takes an ipynb GitHUb link and creates the corresponding NBViewer and Colab links.')
print()

github_link = input('Enter the GitHub link of the ipynb file: ')

colab_link = github_link.replace('github', 'githubtocolab')
nbviewer_link = github_link.replace('github.com/', 'nbviewer.org/github/')

print('Colab')
print(colab_link)
print('NBViewer')
print(nbviewer_link)

print('\nMardown:\n')

print(f'[Colab]({colab_link}) | [NBViewer]({nbviewer_link})')

 


# https://github.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb
# https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb
# https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb
