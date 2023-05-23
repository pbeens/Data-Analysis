# README.md

Welcome to this repository! 

My goal here is to share things I learn about data analysis using Python. The majority of the files I include will likely be Jupyter Notebooks because I like the inherent interactivity Jupyter Notebooks provide, the integration with Markdown (making documentation of the code so much easier), and the ability to easily "chunk" the code to aid in the teaching of how the code works.

# Table of Contents
- [What's New?](#whats-new)
- [Problems Viewing?](#problems-viewing)
- [Miscellaneous](#miscellaneous)
- [Projects](#projects)

# What's New? 

+ I've added [team-roster.ipynb](Sports/NBA/team-roster.ipynb) which uses nba_api data to print some player information for the Toronto Raptors.
+ I've added two glossaries for the nba_api data: [player-stats-glossary.md](Sports/NBA/player-stats-glossary.md) and [team-roster-glossary.md](Sports/NBA/team-roster-glossary.md).
+ I've added [Birth Months](Misc/Birth-Months.ipynb), a program which imports the data from *Google Sheets* and plots a histogram of the birth months.
+ I've added an [FAQ](FAQ.md#how-do-i-create-requirementstxt-for-python) related to the requirements.txt file, which can be used for installing all the required libraries in Python.
+ I've created a [Canadian Population Bar Chart notebook](Wikipedia/Canadian-Population-Barchart.ipynb) ([Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb)) to show how to extract data from a table on a [page](https://en.wikipedia.org/wiki/Population_of_Canada_by_province_and_territory) on Wikipedia. 
+ I've created a Python [utility](Utils/github-to-notebook-links.py) which which will create the Callysto, Colab, and NBViewer links to let you view and/or experiment with a Jupyter notebook that's on GitHub. Look for it in the [Utils](Utils) folder or run it directly [here](https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing).

# Problems Viewing?

Note: if you're having an issue with a Jupyter notebook not displaying in GitHub, go to https://nbviewer.org/ and paste in the URL of the notebook. 

<p align="center">
    <a href="https://nbviewer.org/">
        <img src="images/nbviewer.png" alt="nbviewer" width="75%"/>
    </a>
</p>

Alternatively, you can display the notebook in **Google Colab** by changing the github part of the URL to githubtocolab. https://github.com/ would become https://githubtocolab.com/. 

I have written a utility which will take a GitHub ipynb URL and convert it for use with Colab and NBViewer. You can download the file from [here](Utils/github-to-notebook-links.py) or run it from [here](https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing).

# Miscellaneous 

+ [FAQs](FAQ.md)
+ If you need to quickly code some Python, why not try out JupyterLite? 
<br>[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyter.org/try-jupyter)

# Projects 

+ [Sports/NBA/team-roster.ipynb](Sports/NBA/team-roster.ipynb) — Open in [Callysto](https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https://github.com/pbeens/Data-Analysis&branch=main&subPath=Sports/NBA/team-roster.ipynb&depth=1) | [Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Sports/NBA/team-roster.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Sports/NBA/team-roster.ipynb). The program uses the `nba_api.stats.endpoints` package to access the NBA website and get the roster information for the Toronto Raptors. It then uses the `pandas` library to manipulate and display the data in a tabular format. It uses various pandas attributes, methods, and functions to select, convert, sort, and print the columns of interest. The output shows the names and jersey numbers of the Raptors players in order of their jersey numbers.
+ [Misc/Birth-Months.ipynb](Misc/Birth-Months.ipynb) — Open in 
  [Callysto](https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https://github.com/pbeens/Data-Analysis&branch=main&subPath=Misc/Birth-Months.ipynb&depth=1) | [Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Misc/Birth-Months.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Misc/Birth-Months.ipynb). This Python program uses `pandas` and `matplotlib.pyplot` to read data from a public **Google Sheet**, create a **histogram** of the data in the birth month column, and save the histogram as an **image file**. The program also uses comments to document the code and explain what each line or block of code does. 
+ [Wikipedia/Canadian-Population-Barchart.ipynb](Wikipedia/Canadian-Population-Barchart.ipynb) — Open in [Callysto](https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https://github.com/pbeens/Data-Analysis&branch=main&subPath=Wikipedia/Canadian-Population-Barchart.ipynb&depth=1) | [Colab](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb) | [NBViewer](https://nbviewer.org/github/pbeens/Data-Analysis/blob/main/Wikipedia/Canadian-Population-Barchart.ipynb). This program reads in Canadian population data from a table on a page in **Wikipedia**. It showcases how to read in the data, clean it up so it can be plotted, and then plots two **bar charts**.
