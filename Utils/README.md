# README.md

1. [clipboard-download.ipynb](clipboard-download/clipboard-download.ipynb) is a utility that demonstrates how to use Pandas' `read_clipboard()` method to copy-and-paste table data into your program to create a Pandas dataframe. The program also demonstrates how to save the data to a CSV file

2. [find_table_index.ipynb](find_table_index.ipynb) is a utility that checks for the existence of a table name at a given URL and returns the index of that table. This is useful when scraping data from tables on webpages.<br>You can run this utility directly on Colab [here](https://githubtocolab.com/pbeens/Data-Analysis/blob/main/Utils/find_table_index.ipynb).
   
3. [github-to-notebook-links.py](github-to-notebook-links.py) is a utility that converts a Jupyter Notebook link on GitHub into its corresponding link on Callysto, Colab, and NBViewer. <br>You can run this utility directly on Colab [here](https://colab.research.google.com/drive/12LdduTNAtMwC3oNohv8Y7dFkuJiPYFOd?usp=sharing).
   
4. [ssl-fix.ipynb](ssl-fix.ipynb) is a fix I occasionally need to use when accessing Google Sheets. Simply copy-and-paste this code into your program before reading in the Google Sheet. <br>Note: read the comments in the notebook. There is a fix that I discovered which should make this code obsolete.
   
5. [test-nbformat-version.py](test-nbformat-version.py) is a quick utility used to test which version of nbformat has been installed. This was in support of getting `plotly.express` working.
