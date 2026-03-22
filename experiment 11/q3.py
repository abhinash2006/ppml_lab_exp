#!/usr/bin/env python3
"""
Q3: NumPy array creation, properties, functions.
"""
import numpy as np

print("=== NumPy Array Creation, Properties & Functions ===")


print("\n1. Basic creation:")
zeros = np.zeros((2,3))
ones = np.ones((3,2))
print("zeros(2,3):\n", zeros)
print("ones(3,2):\n", ones)

empty = np.empty((2,2))
print("empty(2,2):\n", empty)

arr_range = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
print("arange(0,10,2):", arr_range)
print("linspace(0,1,5):", linspace)


arr = np.array([[1,2,3],[4,5,6]])
print("\n2. Properties:")
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)
print("Ndim:", arr.ndim)
print("Itemsize:", arr.itemsize)
print("Data type size:", arr.nbytes)

print("\n3. Functions:")
reshaped = arr.reshape(3,2)
print("Reshape to (3,2):\n", reshaped)
print("Flatten:", arr.flatten())

transposed = arr.T
print("Transpose:\n", transposed)

print("\n--- Demo Complete ---")
