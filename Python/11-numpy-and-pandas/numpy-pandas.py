"""
NumPy and Pandas - Data Science Fundamentals

This module covers essential data science libraries:
- NumPy arrays creation and operations
- Array indexing and slicing
- Mathematical operations
- Pandas Series and DataFrames
- Reading and writing data
- Data manipulation and filtering
- GroupBy operations
"""

import numpy as np
import pandas as pd

# ============================================================================
# 1. NUMPY ARRAYS - CREATION AND BASICS
# ============================================================================

print("\n" + "="*70)
print("1. NUMPY ARRAYS - CREATION AND BASICS")
print("="*70)

print("\n--- Creating NumPy Arrays ---")

# From lists
array1 = np.array([1, 2, 3, 4, 5])
print(f"Array from list: {array1}")
print(f"Type: {type(array1)}, Shape: {array1.shape}, Dtype: {array1.dtype}")

# 2D array
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{array2d}")
print(f"Shape: {array2d.shape}")

# Using generators
zeros = np.zeros(5)
print(f"\nZeros: {zeros}")

ones = np.ones((3, 3))
print(f"Ones:\n{ones}")

# Range
range_array = np.arange(0, 10, 2)
print(f"\nRange (0-10, step 2): {range_array}")

# Linspace
linspace_array = np.linspace(0, 1, 5)
print(f"Linspace (0-1, 5 points): {linspace_array}")

# Random
random_array = np.random.rand(3, 3)
print(f"\nRandom array (3x3):\n{random_array}")

# Identity matrix
identity = np.eye(3)
print(f"\nIdentity matrix:\n{identity}")

print("\n--- Array Properties ---")

array = np.array([1, 2, 3, 4, 5, 6])
print(f"Array: {array}")
print(f"Shape: {array.shape}")
print(f"Size: {array.size}")
print(f"Dtype: {array.dtype}")
print(f"Dimensions: {array.ndim}")

# ============================================================================
# 2. ARRAY INDEXING AND SLICING
# ============================================================================

print("\n" + "="*70)
print("2. ARRAY INDEXING AND SLICING")
print("="*70)

print("\n--- 1D Array Indexing ---")

array = np.array([10, 20, 30, 40, 50])
print(f"Array: {array}")
print(f"First element (index 0): {array[0]}")
print(f"Last element (index -1): {array[-1]}")
print(f"Third element (index 2): {array[2]}")

print("\n--- 1D Array Slicing ---")

print(f"array[1:4]: {array[1:4]}")
print(f"array[:3]: {array[:3]}")
print(f"array[2:]: {array[2:]}")
print(f"array[::2]: {array[::2]}")
print(f"array[::-1] (reversed): {array[::-1]}")

print("\n--- 2D Array Indexing ---")

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{array2d}")
print(f"Element at [0, 0]: {array2d[0, 0]}")
print(f"Element at [1, 2]: {array2d[1, 2]}")
print(f"Element at [2, 1]: {array2d[2, 1]}")

print("\n--- 2D Array Slicing ---")

print(f"First row:\n{array2d[0]}")
print(f"Second row:\n{array2d[1]}")
print(f"First column:\n{array2d[:, 0]}")
print(f"Last column:\n{array2d[:, -1]}")
print(f"First 2 rows, first 2 columns:\n{array2d[:2, :2]}")

print("\n--- Boolean Indexing ---")

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {array}")

even_mask = array % 2 == 0
print(f"Even mask: {even_mask}")
print(f"Even numbers: {array[even_mask]}")

greater_than_5 = array > 5
print(f"Numbers > 5: {array[greater_than_5]}")

# ============================================================================
# 3. MATHEMATICAL OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("3. MATHEMATICAL OPERATIONS")
print("="*70)

print("\n--- Element-wise Operations ---")

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"a: {a}")
print(f"b: {b}")
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"b / a: {b / a}")
print(f"a ** 2: {a ** 2}")

print("\n--- Array with Scalar ---")

array = np.array([1, 2, 3, 4, 5])
print(f"Array: {array}")
print(f"Array + 10: {array + 10}")
print(f"Array * 2: {array * 2}")

print("\n--- Aggregate Functions ---")

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {array}")
print(f"Sum: {np.sum(array)}")
print(f"Mean: {np.mean(array)}")
print(f"Median: {np.median(array)}")
print(f"Std Dev: {np.std(array)}")
print(f"Min: {np.min(array)}")
print(f"Max: {np.max(array)}")

print("\n--- 2D Array Operations ---")

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{array2d}")
print(f"Sum all: {np.sum(array2d)}")
print(f"Sum along rows (axis 1):\n{np.sum(array2d, axis=1)}")
print(f"Sum along columns (axis 0):\n{np.sum(array2d, axis=0)}")
print(f"Mean along axis 0:\n{np.mean(array2d, axis=0)}")

print("\n--- Linear Algebra ---")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(f"Matrix a:\n{a}")
print(f"Matrix b:\n{b}")
print(f"Matrix multiplication (dot product):\n{np.dot(a, b)}")

# ============================================================================
# 4. PANDAS SERIES
# ============================================================================

print("\n" + "="*70)
print("4. PANDAS SERIES")
print("="*70)

print("\n--- Creating Series ---")

# From list
series1 = pd.Series([10, 20, 30, 40, 50])
print(f"Series from list:\n{series1}")

# With custom index
series2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(f"\nSeries with custom index:\n{series2}")

# From dictionary
data_dict = {'apple': 5, 'banana': 3, 'orange': 7}
series3 = pd.Series(data_dict)
print(f"\nSeries from dictionary:\n{series3}")

print("\n--- Series Indexing ---")

series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(f"Series:\n{series}")
print(f"series['a']: {series['a']}")
print(f"series[0]: {series[0]}")
print(f"series[['a', 'c', 'e']]:\n{series[['a', 'c', 'e']]}")

print("\n--- Series Operations ---")

series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(f"Series1:\n{series1}")
print(f"Series2:\n{series2}")
print(f"Series1 + Series2:\n{series1 + series2}")

print("\n--- Series Statistics ---")

series = pd.Series([10, 20, 30, 40, 50, 60])
print(f"Series: {series.values}")
print(f"Sum: {series.sum()}")
print(f"Mean: {series.mean()}")
print(f"Std: {series.std()}")
print(f"Min: {series.min()}")
print(f"Max: {series.max()}")

# ============================================================================
# 5. PANDAS DATAFRAMES
# ============================================================================

print("\n" + "="*70)
print("5. PANDAS DATAFRAMES")
print("="*70)

print("\n--- Creating DataFrames ---")

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 75000, 80000]
}
df = pd.DataFrame(data)
print(f"DataFrame from dictionary:\n{df}")

print("\n--- DataFrame Info ---")

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")
print(f"Dtypes:\n{df.dtypes}")

print("\n--- Accessing Data ---")

print(f"df['Name']:\n{df['Name']}")
print(f"\ndf['Age']:\n{df['Age']}")
print(f"\ndf.loc[0]:\n{df.loc[0]}")
print(f"\ndf.iloc[1]:\n{df.iloc[1]}")

print("\n--- DataFrame Operations ---")

print(f"Mean age: {df['Age'].mean()}")
print(f"Total salary: {df['Salary'].sum()}")
print(f"Max age: {df['Age'].max()}")

# ============================================================================
# 6. DATA MANIPULATION AND FILTERING
# ============================================================================

print("\n" + "="*70)
print("6. DATA MANIPULATION AND FILTERING")
print("="*70)

print("\n--- Creating Sample DataFrame ---")

df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Price': [1.0, 0.5, 2.0, 3.0, 4.0],
    'Quantity': [10, 20, 15, 5, 8],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit']
})
print(f"DataFrame:\n{df}")

print("\n--- Adding Columns ---")

df['Total'] = df['Price'] * df['Quantity']
print(f"\nDataFrame with Total column:\n{df}")

print("\n--- Filtering ---")

expensive = df[df['Price'] > 1.5]
print(f"\nProducts with Price > 1.5:\n{expensive}")

high_quantity = df[df['Quantity'] >= 10]
print(f"\nProducts with Quantity >= 10:\n{high_quantity}")

print("\n--- Multiple Conditions ---")

filtered = df[(df['Price'] > 1.0) & (df['Quantity'] > 10)]
print(f"\nPrice > 1.0 AND Quantity > 10:\n{filtered}")

print("\n--- Modifying Values ---")

df_copy = df.copy()
df_copy.loc[0, 'Price'] = 1.5
print(f"\nAfter modifying first row Price:\n{df_copy[['Product', 'Price']]}")

print("\n--- Dropping Columns/Rows ---")

df_reduced = df.drop('Category', axis=1)
print(f"\nDataFrame without Category column:\n{df_reduced}")

# ============================================================================
# 7. GROUPBY OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("7. GROUPBY OPERATIONS")
print("="*70)

print("\n--- Creating Sample Data ---")

sales_data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['A', 'B', 'A', 'B', 'B', 'A'],
    'Sales': [1000, 1500, 1200, 1100, 1300, 1400]
})
print(f"Sales Data:\n{sales_data}")

print("\n--- GroupBy Single Column ---")

region_sales = sales_data.groupby('Region')['Sales'].sum()
print(f"\nTotal sales by region:\n{region_sales}")

print("\n--- GroupBy Multiple Aggregations ---")

grouped = sales_data.groupby('Region')['Sales'].agg(['sum', 'mean', 'count'])
print(f"\nAggregations by region:\n{grouped}")

print("\n--- GroupBy Multiple Columns ---")

grouped = sales_data.groupby(['Region', 'Product'])['Sales'].sum()
print(f"\nSales by region and product:\n{grouped}")

print("\n--- Custom Aggregation ---")

def custom_agg(x):
    return {
        'Total': x.sum(),
        'Average': x.mean(),
        'Count': x.count()
    }

grouped = sales_data.groupby('Region')['Sales'].apply(custom_agg)
print(f"\nCustom aggregation:\n{grouped}")

# ============================================================================
# 8. READING AND WRITING DATA
# ============================================================================

print("\n" + "="*70)
print("8. READING AND WRITING DATA")
print("="*70)

print("""
Common file formats for Pandas:

CSV (Comma-Separated Values):
  df = pd.read_csv('file.csv')
  df.to_csv('output.csv', index=False)

Excel:
  df = pd.read_excel('file.xlsx')
  df.to_excel('output.xlsx', index=False)

JSON:
  df = pd.read_json('file.json')
  df.to_json('output.json')

SQL:
  df = pd.read_sql('SELECT * FROM table', connection)
  df.to_sql('table_name', connection)

Parquet (efficient binary format):
  df = pd.read_parquet('file.parquet')
  df.to_parquet('output.parquet')

HDF5:
  df = pd.read_hdf('file.h5')
  df.to_hdf('output.h5', 'key')
""")

print("\n--- CSV Example ---")

# Create sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# Save to CSV
df.to_csv('sample.csv', index=False)
print(f"Saved DataFrame to sample.csv")

# Read back
df_read = pd.read_csv('sample.csv')
print(f"\nRead DataFrame from sample.csv:\n{df_read}")

# Cleanup
import os
os.remove('sample.csv')

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. NumPy Array Operations:
   - Create arrays using different methods
   - Perform mathematical operations
   - Use boolean indexing
   - Calculate statistics
   - Reshape and transpose arrays

2. Pandas Series:
   - Create Series with different index types
   - Perform arithmetic operations between Series
   - Calculate statistics
   - Filter based on conditions
   - Sort by values and index

3. Pandas DataFrame:
   - Create from different sources (dict, list, arrays)
   - Add and remove columns
   - Filter rows based on conditions
   - Sort by multiple columns
   - Access data using loc and iloc

4. Data Manipulation:
   - Clean data (handle missing values)
   - Create new columns based on existing ones
   - Rename columns
   - Merge/join DataFrames
   - Concatenate DataFrames

5. Analysis Exercise:
   - Load sample dataset
   - Explore structure (shape, dtypes, missing values)
   - Calculate summary statistics
   - Group by category
   - Create pivot tables
   - Generate insights about the data
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
