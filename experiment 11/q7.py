#!/usr/bin/env python3
"""
Q7: Create and manipulate Pandas data.
Sort, filter, add/drop columns/rows, groupby.
"""
import pandas as pd
import numpy as np

print("=== Pandas Data Manipulation ===")

# Create df
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "Salary": [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print("\nOriginal DF:\n", df)

# Add column
df["Bonus"] = df["Salary"] * 0.1
print("\nAdded Bonus:\n", df)

# Sort
print("\nSorted by Age:\n", df.sort_values("Age"))

# Filter
print("\nAge > 28:\n", df[df["Age"] > 28])

# Groupby
df["Dept"] = ["HR", "IT", "HR", "IT"]
print("\nGroupby Dept mean Salary:\n", df.groupby("Dept")["Salary"].mean())

# Drop
df_dropped = df.drop("Bonus", axis=1)
print("\nDropped Bonus:\n", df_dropped)

# Set index
df_indexed = df.set_index("Name")
print("\nSet index Name:\n", df_indexed)

print("\n--- Demo Complete ---")
