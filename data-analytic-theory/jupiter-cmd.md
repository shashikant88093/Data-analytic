# loc method
- The `loc` method in pandas is used to access a group of rows and columns by labels or a boolean array. It is primarily label-based indexing, which means that you can use the row and column labels to select data.
- The syntax for using `loc` is as follows:
```python
df.loc[row_labels, column_labels]
```
- Here, `row_labels` can be a single label, a list of labels, or a slice object, and `column_labels` can be a single label or a list of labels.


# What is not allowed in jupiter Notebokk cells ?

- In Jupyter Notebook cells, certain operations and commands are not allowed or may not work as expected. These include:
  - **Shell commands**: Direct shell commands (like `ls`, `cd`, etc.) are not executed unless prefixed with an exclamation mark (`!`).
  - **File system operations**: Direct file system operations (like reading or writing files) may require specific permissions or paths.
  - **Non-Python code**: Cells must contain valid Python code; other languages require specific magic commands (e.g., `%%bash` for Bash).
  - **Interactive widgets**: Some interactive widgets may not function properly without the appropriate setup or extensions.
  - An excel file cannot be opened directly in a Jupyter Notebook cell. Instead, you can use libraries like `pandas` to read and manipulate Excel files. For example:
```python
import pandas as pd
df = pd.read_excel('file.xlsx')
df.head()
```

# What is the difference between `loc` and `iloc` in pandas?
- The `loc` and `iloc` methods in pandas are used for data selection, but they differ in how they access data:
  - **`loc`**: This method is label-based, meaning it accesses rows and columns by their labels (index names). It includes the end label in the selection.
    ```python
    df.loc['row_label', 'column_label']
    ```
  - **`iloc`**: This method is integer-location based, meaning it accesses rows and columns by their integer index positions. It does not include the end position in the selection.
    ```python
    df.iloc[0:5, 0:2]  # Selects the first 5 rows and first 2 columns
    ```


# What is the purpose of the `head()` method in pandas?
- The `head()` method in pandas is used to return the first n rows of a Data
- Frame. By default, it returns the first 5 rows, but you can specify a different number by passing an integer argument.
```python
df.head(n)  # Returns the first n rows of the DataFrame
```
- This method is useful for quickly inspecting the structure and contents of a DataFrame without displaying the entire dataset, especially when dealing with large datasets.

# What are the three main types of Jupyter Notebook Cell ?

- Jupyter Notebook cells can be categorized into three main types:
  - **Code Cells**: These cells contain executable code, typically in Python, but can also support other languages. When executed, the code runs, and the output is displayed below the cell.
  - **Markdown Cells**: These cells are used for documentation and can contain formatted text, images, links, and LaTeX equations. They are useful for adding explanations, comments, and descriptions to the notebook.
  - **Raw Cells**: These cells contain raw text that is not processed by the notebook. They are typically used for including text that should not be formatted or executed, such as plain text notes or code snippets that are not meant to be run.

#What kind of data can you import and work with in a Jupyter Notebook?
- In a Jupyter Notebook, you can import and work with various types of data, including:
  - **CSV files**: Comma-separated values files can be read using libraries like `pandas`.
  - **Excel files**: Excel spreadsheets can be imported using `pandas` or `openpyxl`.
  - **JSON files**: JavaScript Object Notation files can be read using the `json` module or `pandas`.
  - **SQL databases**: Data can be queried from SQL databases using libraries like `sqlite3` or `SQLAlchemy`.
  - **Text files**: Plain text files can be read using built-in Python functions.
  - **Images and multimedia**: Libraries like `PIL` (Pillow) or `OpenCV` can be used to work with images and videos.
  - **APIs**: Data can be fetched from web APIs using libraries like `requests`.    