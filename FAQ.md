# FAQs

These FAQs will be used to record any general things I find interesting about data analysis that I learn along the way. 

# Table of Contents
- [What is the difference between print() and display() in Jupyter notebooks?](#what-is-the-difference-between-print-and-display-in-jupyter-notebooks)
- [Why is it preferable to use underscores between the words of a Pandas header?](#why-is-it-preferable-to-use-underscores-between-the-words-of-a-pandas-header)
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

# What VS Code Extensions Do I Like?

+ [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight): Highlight TODO, FIXME and other annotations within your code.
+ [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): This extension quickly searches your workspace for comment tags like TODO and FIXME and displays them in a tree view in the activity bar. Clicking a TODO within the tree will open the file and put the cursor on the line containing the TODO.