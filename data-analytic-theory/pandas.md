# whats is pandas?
- Pandas is a powerful open-source data analysis and manipulation library for Python. It provides data structures like Series and DataFrame, which are designed to handle structured data efficiently. Pandas is widely used in data science, machine learning, and statistical analysis due to its flexibility and ease of use.

# How to install pandas?
- Pandas can be installed using pip, the Python package manager. You can install it by running the following command in your terminal or command prompt:
```bash
pip install pandas
```

- Alternatively, if you are using Anaconda, you can install pandas using the following command:
```bash
conda install pandas
```

# How to import pandas in Python?
- To use pandas in your Python code, you need to import it first. The conventional way to import pandas is as follows:
```python
import pandas as pd
```                                                         
- This imports the pandas library and allows you to use the alias `pd` to access its functions and classes, making your code more concise.
# What is the purpose of the `DataFrame` in pandas?
- The `DataFrame` is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure in pandas. It is similar to a spreadsheet or SQL table and is used to store and manipulate structured data. The `DataFrame` allows for easy indexing, slicing, and aggregation of data, making it a powerful tool for data analysis.

# How to create a DataFrame in pandas?
- You can create a DataFrame in pandas using various methods, such as from a dictionary, a list of lists, or by reading data from a file (like CSV or Excel). Here are some examples:
```python
import pandas as pd
# From a dictionary
data = {    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# From a list of lists
data = [['Alice', 25, 'New York'], ['Bob', 30, '
Los Angeles'], ['Charlie', 35, 'Chicago']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
# From a CSV file
df = pd.read_csv('data.csv')  # Assuming 'data.csv' is a valid CSV file
```


# pandas conditional selection
- In pandas, you can perform conditional selection on DataFrames using boolean indexing. This allows you to filter rows based on specific conditions. For example, if you have a DataFrame `df` and you want to select rows where the value in the column 'A' is greater than 10, you can do it as follows:
```python
import pandas as pd
df = pd.DataFrame({'A': [5, 15, 25], 'B': [10, 20, 30]})
selected_rows = df[df['A'] > 10]    
print(selected_rows)
```
- This will return a new DataFrame containing only the rows where the condition is met. You can also combine multiple conditions using logical operators like `&` (and) and `|` (or). For example:
```python
selected_rows = df[(df['A'] > 10) & (df['B'] < 30)]
print(selected_rows)
```
