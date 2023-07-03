# README.md

This was a bit if a bust. When opening a notebook with the newly generated ToC [(using my automated approach)](create-jupyter-notebook-toc.py) in Callysto I would get this error:

`Notebook validation failed: Additional properties are not allowed ('id' was unexpected):
{
 "attachments": {},
 "cell_type": "markdown",
 "id": "04ceb7da",
 "metadata": {},
 "source": "# Table of Contents\n\n"
}`

In Colab and Callysto, I didn't get any errors but the anchor links didn't work.

In GitHib, the anchor links returned us to directory of the repo.

I tried [manually enter](create-jupyter-notebook-toc-v2.py) the created ToC as well. The only difference that made was there was no error when opening it in Callysto, but the anchor links still didn't do anything.

ChatGPT tells me this has something to do with the rendering engines of Callysto, Colab, and GitHub, but it's beyond my capabilities to get it working.

It would have been nice to get this working. Perhaps someone else can make it work.

## Example ToC Content

```
# Table of Contents

- [Introduction to Python Programming](#introduction-to-python-programming)
- [What is Python?](#what-is-python?)
- [Variables and Data Types](#variables-and-data-types)
    - [Assigning Values to Variables](#assigning-values-to-variables)
    - [Variable Naming Rules](#variable-naming-rules)
    - [Common Data Types](#common-data-types)
    - [Examples](#examples)
- [Control Flow and Decision-Making](#control-flow-and-decision-making)
    - [Conditional Statements (if-else)](#conditional-statements-(if-else))
    - [elif Statements](#elif-statements)
    - [Comparison Operators](#comparison-operators)
- [Iteration in Python: Repeating Code Blocks](#iteration-in-python:-repeating-code-blocks)
    - [Looping Through a Range](#looping-through-a-range)
    - [while Loop](#while-loop)
- [Conclusion](#conclusion)
  ```