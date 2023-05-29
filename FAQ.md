# FAQs

These FAQs will be used to record any general things I find interesting about data analysis that I learn along the way. 

# Table of Contents
- [What is the difference between print() and display() in Jupyter notebooks?](#what-is-the-difference-between-print-and-display-in-jupyter-notebooks)
- [Why is it preferable to use underscores between the words of a Pandas header?](#why-is-it-preferable-to-use-underscores-between-the-words-of-a-pandas-header)
- [Explain how the index in a Pandas dataframe works.](#explain-how-the-index-in-a-pandas-dataframe-works)
- [How can we display a Pandas dataframe without the index?](#how-can-we-display-a-pandas-dataframe-without-the-index)
- [How do I create requirements.txt for Python?](#how-do-i-create-requirementstxt-for-python)
- [How can I use requirements.txt to install the necessary libraries?](#how-can-i-use-requirementstxt-to-install-the-necessary-libraries)
- [What are some good websites for open data?](#what-are-some-good-websites-for-open-data)
- [What VS Code extensions do I like?](#what-vs-code-extensions-do-i-like)


# What is the difference between print() and display() in Jupyter notebooks?

The difference between **print()** and **display()** in Python notebooks is that **print()** is the standard Python function that prints a text representation of an object to the standard output, while **display()** is a special function provided by IPython that can display rich representations of various types of objects, such as images, videos, HTML, etc¹².

For example, if you have an image object called img, you can use **print(img)** to print the text representation of the image object, such as its shape, size, mode, etc. However, if you use **display(img)**, you will see the actual image displayed in the notebook cell.

Another difference is that **print()** always returns None, while **display()** can return a display object that can be further manipulated or updated².

A third difference is that **print()** can only print one object per line, while **display()** can display multiple objects in a single line².

A final difference is that when you just write the variable name on the last line of a cell, it will automatically call **display()** on that variable name and show its rich representation². This is a convenient shorthand for interactive exploration. However, if you want to print the text representation of the variable name, you need to explicitly use **print()**.

Source: Conversation with Bing, 2023-05-21
1. scheme - Difference between Print and Display - Stack Overflow. https://stackoverflow.com/questions/956969/difference-between-print-and-display.
2. Jupyter Notebook different ways to display out - Stack Overflow. https://stackoverflow.com/questions/54097882/jupyter-notebook-different-ways-to-display-out.

# Why is it preferable to use underscores between the words of a Pandas header?

It is preferable to use underscores between the words of a Pandas header because it makes the header easier to use and manipulate in code. For example, if you have a header like "Primary Channel", you would need to use quotes and brackets to access it as a column name, such as df["Primary Channel"]. However, if you use underscores instead, like "Primary_Channel", you can access it as an attribute, such as df.Primary_Channel¹.

Using underscores also avoids potential errors or confusion caused by spaces in the header names. For example, if you have a header like "New Members", it could be interpreted as two separate headers, "New" and "Members", by some functions or methods². Spaces can also cause problems when saving or loading data from different formats, such as CSV or JSON³.

Therefore, it is a good practice to use underscores instead of spaces in Pandas headers. You can use various methods to remove or replace spaces in the headers, such as str.replace, str.strip, str.lstrip, str.rstrip, add_prefix, rename, etc²⁴⁵.

Source: Conversation with Bing, 2023-05-21
1. [Code]-Pandas Function to Add Underscore to all Column Headers in a .... https://www.appsloveworld.com/pandas/100/482/pandas-function-to-add-underscore-to-all-column-headers-in-a-dataframe.
2. Pandas Function to Add Underscore to all Column Headers in a DataFrame .... https://stackoverflow.com/questions/61233778/pandas-function-to-add-underscore-to-all-column-headers-in-a-dataframe.
3. Remove or replace spaces in column names - Stack Overflow. https://stackoverflow.com/questions/41476150/remove-or-replace-spaces-in-column-names.
4. pandas replace column name spaces with underscore - GrabThisCode. https://grabthiscode.com/python/pandas-replace-column-name-spaces-with-underscore.
5. How to remove underscores from column names within plots?. https://stackoverflow.com/questions/70312813/how-to-remove-underscores-from-column-names-within-plots.

# Explain how the index in a Pandas dataframe works.

The index in a Pandas DataFrame is a special object that labels the rows of the DataFrame. It can be either a single column of values, such as integers or strings, or a multi-level index that consists of multiple columns of values. The index can be used to access and modify the rows of the DataFrame in various ways, such as slicing, filtering, sorting, grouping, etc¹².

The index can be set when creating a DataFrame from scratch or from an existing data source, such as a CSV file or a database. You can also change the index of an existing DataFrame by using methods such as set_index, reset_index, reindex, etc¹³. The index can have a name or names that describe its meaning or source⁴.

The index is an important feature of Pandas DataFrames because it enables fast and efficient data alignment and operations. For example, when performing arithmetic operations or merging DataFrames, Pandas will automatically align the data by matching the index labels of the operands¹⁵. This ensures that the data is consistent and accurate across different DataFrames. The index also provides metadata for the DataFrame that can be useful for analysis, visualization, and interactive console display¹.

Source: Conversation with Bing, 2023-05-21
1. pandas.DataFrame.index — pandas 2.0.1 documentation. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html.
2. Indexing and selecting data — pandas 2.0.1 documentation. https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html.
3. Tutorial: How to Index DataFrames in Pandas - Dataquest. https://www.dataquest.io/blog/tutorial-indexing-dataframes-in-pandas/.
4. Indexing and Selecting Data with Pandas - GeeksforGeeks. https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/.
5. Pandas Dataframe Index in Python - PythonForBeginners.com. https://www.pythonforbeginners.com/basics/pandas-dataframe-index-in-python.

# How can we display a Pandas dataframe without the index?

There are a few ways to display a Pandas dataframe without the index. One way is to use the `to_string` method with the `index=False` parameter. For example:

```python
print(df.to_string(index=False))
```

This will print the dataframe as a string without the index column¹²³.

Another way is to use the `style` property with the `hide_index` method. For example:

```python
df.style.hide_index()
```

This will return a styled object that hides the index column when displayed²⁴. (Note: This requires the installation of Jinja2.) 

A third way is to use the `to_html` method with the `index=False` parameter and display it as HTML. For example:

```python
from IPython.display import HTML
HTML(df.to_html(index=False))
```

This will display the dataframe as an HTML table without the index column⁵.

Source: Conversation with Bing, 2023-05-23
1. Display pandas dataframe without index - Stack Overflow. https://stackoverflow.com/questions/64846520/display-pandas-dataframe-without-index.
2. How to print pandas DataFrame without index - Stack Overflow. https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index.
3. How to print Dataframe in Python without Index? - GeeksforGeeks. https://www.geeksforgeeks.org/how-to-print-dataframe-in-python-without-index/.
4. How to Print Pandas DataFrame without Index - Spark By Examples. https://sparkbyexamples.com/pandas/print-pandas-dataframe-without-index/.
5. Display full Pandas dataframe in Jupyter without index. https://stackoverflow.com/questions/63234174/display-full-pandas-dataframe-in-jupyter-without-index.

# How do I create requirements.txt for Python?

A requirements.txt file is a text file that lists the Python packages and their versions that are required for a Python project. It is useful for managing dependencies and sharing your project with others.

There are different ways to create a requirements.txt file, depending on your situation. Here are some common methods:

- Assuming you have already installed the packages in your virtual environment or system, you can use the `pip freeze` command to generate a requirements.txt file with the exact versions of the installed packages. For example:

```bash
pip freeze > requirements.txt
```

This will create a requirements.txt file in your current directory with the output of `pip freeze`.

For more information about requirements.txt files, you can visit this link: https://packaging.python.org/tutorials/installing-packages/#requirements-files

Source: Conversation with Bing, 2023-05-22
1. The Python Requirements File and How to Create it. https://learnpython.com/blog/python-requirements-file/.
2. python - Automatically create requirements.txt - Stack Overflow. https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt.
3. python - How to check requirements and generate a requirements.txt file .... https://stackoverflow.com/questions/65261513/how-to-check-requirements-and-generate-a-requirements-txt-file.
4. How to Create Requirements.txt Python? - Scaler. https://www.scaler.com/topics/how-to-create-requirements-txt-python/.

# How can I use requirements.txt to install the necessary libraries?

To install the packages from a requirements.txt file, you can use the `pip install` command with the `-r` option. For example:

```bash
pip install -r requirements.txt
```

This will install all the packages and their versions that are listed in the requirements.txt file. 

You can also use the `--upgrade` option to upgrade the packages to their latest versions, regardless of what is specified in the requirements.txt file. For example:

```bash
pip install --upgrade -r requirements.txt
```

This will install or upgrade all the packages to their latest versions.

# What are some good websites for open data?

Open data websites are online platforms that provide access to data that is **free** to use, reuse, or share⁴. Open data can come from various sources, such as governments, organizations, research institutions, and individuals⁴. Some examples of open data websites are:

- **Open Data | Open Government, Government of Canada**¹: This website offers open data from the Canadian government on various topics, such as agriculture, economics, health, and environment¹.
- **Google Dataset Search**²: This website allows you to search for datasets across the web using Google's search engine². You can filter by format, license, provider, and update date².
- **Open data - Wikipedia**³: This website provides a list of open data initiatives and websites from different countries and regions around the world³.
- **40 Places to Find Open Data on the Web - Rock Content**⁴: This website provides a curated list of 40 open data websites covering various domains, such as business, education, sports, and social media⁴.
- **55 Free Open Data Sources You Should Know**⁵: This website provides another curated list of 55 open data websites with brief descriptions and links⁵.

Source: Conversation with Bing, 2023-05-29
1. Open Data | Open Government, Government of Canada. https://open.canada.ca/en/open-data.
2. 10 Great Places To Find Open, Free Datasets [2023 Guide] - CareerFoundry. https://careerfoundry.com/en/blog/data-analytics/where-to-find-free-datasets/.
3. Open data - Wikipedia. https://en.wikipedia.org/wiki/Open_data.
4. 40 Places to Find Open Data on the Web - Rock Content. https://rockcontent.com/blog/data-sources/.
5. 55 Free Open Data Sources You Should Know. https://data-ox.com/55-free-open-data-sources-you-should-know-for-2021.

# What VS Code extensions do I like?

+ [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight): Highlight TODO, FIXME and other annotations within your code.
+ [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): This extension quickly searches your workspace for comment tags like TODO and FIXME and displays them in a tree view in the activity bar. Clicking a TODO within the tree will open the file and put the cursor on the line containing the TODO.