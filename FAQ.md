# FAQs

These FAQs will be used to record any general things I find interesting about data analysis that I learn along the way. 

# Table of Contents
- [What is the difference between print() and display() in Jupyter notebooks?](#what-is-the-difference-between-print-and-display-in-jupyter-notebooks)
- [Why is it preferable to use underscores between the words of a Pandas header?](#why-is-it-preferable-to-use-underscores-between-the-words-of-a-pandas-header)
- [Explain how the index in a Pandas dataframe works.](#explain-how-the-index-in-a-pandas-dataframe-works)
- [How do I create requirements.txt for Python?](#how-do-i-create-requirementstxt-for-python)
- [How can I used requirements.txt to install the necessary libraries?](#how-can-i-used-requirementstxt-to-install-the-necessary-libraries)
- [What VS Code Extensions Do I Like?](#what-vs-code-extensions-do-i-like)

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

# How can I used requirements.txt to install the necessary libraries?

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

# What VS Code Extensions Do I Like?

+ [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight): Highlight TODO, FIXME and other annotations within your code.
+ [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): This extension quickly searches your workspace for comment tags like TODO and FIXME and displays them in a tree view in the activity bar. Clicking a TODO within the tree will open the file and put the cursor on the line containing the TODO.