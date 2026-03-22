#!/usr/bin/env python3
"""
Q1: Write a program for N-D NumPy array object, indexing and slicing.
Demonstrates creation of 1D, 2D, 3D arrays, basic/advanced indexing, slicing.
"""
import numpy as np

print("=== NumPy N-D Array: Indexing &amp; Slicing ===")

# 1D array
arr1d = np.array([0, 1, 2, 3, 4, 5])
print("\n1D Array:", arr1d)
print("Indexing: arr1d[2] =", arr1d[2])
print("Slicing: arr1d[1:4] =", arr1d[1:4])
print("Negative indexing: arr1d[-2] =", arr1d[-2])

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:\n", arr2d)
print("Row indexing: arr2d[1] =", arr2d[1])
print("Element: arr2d[1,2] =", arr2d[1,2])
print("Slicing rows: arr2d[0:2] =\n", arr2d[0:2])
print("Slicing columns: arr2d[:,1] =", arr2d[:,1])
print("Subarray: arr2d[1:3,1:3] =\n", arr2d[1:3,1:3])

# 3D array
arr3d = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print("\n3D Array shape:", arr3d.shape)
print("3D slice: arr3d[0,:,:] =\n", arr3d[0,:,:])
print("Advanced indexing: arr3d[[0,1],[0,1],[0,1]] =", arr3d[[0,1],[0,1],[0,1]])

# Boolean indexing
arr = np.array([10, 20, 30, 40, 50])
print("\nBoolean indexing: >30 =", arr[arr > 30])

print("\n--- Demo Complete ---")
