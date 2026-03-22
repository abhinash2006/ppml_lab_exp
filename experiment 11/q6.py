#!/usr/bin/env python3
"""
Q6: Create and work with Pandas DataFrames.
From dict/list, view info, select columns/rows.
"""
import pandas as pd
import numpy as np

print("=== Pandas DataFrames: Create & Work ===")

# From dict
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "SF"]
}
df = pd.DataFrame(data)
print("\nDataFrame from dict:\n", df)

# From list/np array
data2 = np.random.randn(4,3)
df2 = pd.DataFrame(data2, columns=["A", "B", "C"])
print("\nFrom np.array:\n", df2.head())

# Properties
print("\nInfo:")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())
print("dtypes:\n", df.dtypes)

# Select
print("\nSelections:")
print("Column 'Age':\n", df["Age"])
print("Rows 0:2:\n", df.iloc[0:2])
print("Name == 'Bob':\n", df[df["Name"] == "Bob"])

print("\n--- Demo Complete ---")
