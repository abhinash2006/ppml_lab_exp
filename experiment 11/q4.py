#!/usr/bin/env python3
"""
Q4: Statistical operations on NumPy arrays.
Uses np.mean, std, min, max, sum, etc. axis-wise.
"""
import numpy as np

print("=== NumPy Statistical Operations ===")

data = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("\nData:\n", data)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std dev:", np.std(data))
print("Variance:", np.var(data))

print("\nAxis-wise:")
print("Row means:", np.mean(data, axis=1))
print("Col means:", np.mean(data, axis=0))
print("Row sums:", np.sum(data, axis=1))
print("Min per col:", np.min(data, axis=0))
print("Max per row:", np.max(data, axis=1))

# Cumulative
print("\nCumulative sum:", np.cumsum(data.flatten()))

# Percentiles
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))

# Correlation
a = np.array([1,2,3])
b = np.array([2,4,5])
print("Correlation coeff:", np.corrcoef(a,b)[0,1])

print("\n--- Demo Complete ---")
