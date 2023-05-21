# FAQs

# Table of Contents
- [What is the difference between print() and display() in Juoyter notebooks?](#what-is-the-difference-between-print-and-display-in-juoyter-notebooks)

# What is the difference between print() and display() in Juoyter notebooks?

The difference between **print()** and **display()** in Python notebooks is that **print()** is the standard Python function that prints a text representation of an object to the standard output, while **display()** is a special function provided by IPython that can display rich representations of various types of objects, such as images, videos, HTML, etc¹².

For example, if you have an image object called img, you can use **print(img)** to print the text representation of the image object, such as its shape, size, mode, etc. However, if you use **display(img)**, you will see the actual image displayed in the notebook cell.

Another difference is that **print()** always returns None, while **display()** can return a display object that can be further manipulated or updated².

A third difference is that **print()** can only print one object per line, while **display()** can display multiple objects in a single line².

A final difference is that when you just write the variable name on the last line of a cell, it will automatically call **display()** on that variable name and show its rich representation². This is a convenient shorthand for interactive exploration. However, if you want to print the text representation of the variable name, you need to explicitly use **print()**.

Source: Conversation with Bing, 2023-05-21
1. scheme - Difference between Print and Display - Stack Overflow. https://stackoverflow.com/questions/956969/difference-between-print-and-display.
2. Jupyter Notebook different ways to display out - Stack Overflow. https://stackoverflow.com/questions/54097882/jupyter-notebook-different-ways-to-display-out.