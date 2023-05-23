# README.md

Welcome to this repository! 

My goal here is to share things I learn about data analysis using Python. The majority of the files I include will likely be Jupyter Notebooks because I like the inherent interactivity Jupyter Notebooks provide, the integration with Markdown (making documentation of the code so much easier), and the ability to easily "chunk" the code to aid in the teaching of how the code works.

# What's New? 

+ I've added [Birth Months](Misc/Birth-Months.ipynb), a program which imports the data from *Google Sheets* and plots a histogram of the birth months.
+ I've added an [FAQ](FAQ.md#how-do-i-create-requirementstxt-for-python) related to the requirements.txt file, which can be used for installing all the required libraries in Python.
+ I've created a [Canadian Population Barchart notebook](Wikipedia/Canadian-Population-Barchart.ipynb) ([Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb)) to show how to extract data from a table on a [page](https://en.wikipedia.org/wiki/Population_of_Canada_by_province_and_territory) on Wikipedia. 
+ I've created a Python [utility](Utils/github-to-nbviewer-and-colab-links.py) which which will create the Colab and NBViewer links to let you view and/or experiment with a Jupyter notebook that's on GitHub. Look for it in the [Utils](Utils) folder or run it directly [here](https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing).

# Problems Viewing?

Note: if you're having an issue with a Jupyter notebook not displaying in GitHub, go to https://nbviewer.org/ and paste in the URL of the notebook. 

<div style="text-align: center;">
<a href="https://nbviewer.org/">
<img src="images/nbviewer.png" alt="nbviewer" width="75%"/>
</a>
</div>

Alternatatively, you can display the notebook in **Google Colab** by changing the github part of the URL to githubtocolab. https://github.com/ would become https://githubtocolab.com/. 

I have written a utility which will take a GitHub ipynb URL and convert it for use with Colab and NBViewer. You can download the file from [here](Utils/github-to-nbviewer-and-colab-links.py).

# Miscellaneous 

+ [FAQs](FAQ.md)
+ If you need to quickly code some Python, why not try out JupyterLite? 
<br>[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyter.org/try-jupyter)

# Projects 

+ [Misc/Birth-Months.ipynb](Misc/Birth-Months.ipynb) — Open in [Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Misc/Birth-Months.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Misc/Birth-Months.ipynb). This Python program uses pandas and matplotlib.pyplot to read data from a public Google Sheet, create a histogram of the data in the birth month column, and save the histogram as an image file. The program also uses comments to document the code and explain what each line or block of code does. 
+ [Wikipedia/Canadian-Population-Barchart.ipynb](Wikipedia/Canadian-Population-Barchart.ipynb) — Open in [Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb). This program reads in Canadian population data from a table on a page in Wikipedia. It showcases how to read in the data, clean it up so it can be plotted, and then plots two bar charts. 
