#!/usr/bin/env python3
"""
Q5: Saving and loading NumPy arrays, error handling.
Uses np.save, np.load, try-except for common errors.
"""
import numpy as np
import os

print("=== NumPy Save/Load with Error Handling ===")

arr = np.array([[1,2],[3,4]])

# Save
filename = "test_array.npy"
try:
    np.save(filename, arr)
    print(f"Saved array to {filename}")
except Exception as e:
    print(f"Save error: {e}")

# Load
try:
    loaded = np.load(filename)
    print("Loaded array:\n", loaded)
    print("Original == Loaded:", np.array_equal(arr, loaded))
except FileNotFoundError:
    print("Error: File not found (save first)")
except Exception as e:
    print(f"Load error: {e}")

# .npz for multiple
arrays = {"a": arr, "b": arr*2}
try:
    np.savez("multi_arrays.npz", **arrays)
    print("Saved multiple to multi_arrays.npz")
    
    data = np.load("multi_arrays.npz")
    print("Loaded a:\n", data["a"])
except Exception as e:
    print(f"npz error: {e}")

# Cleanup
for f in [filename, "multi_arrays.npz"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned {f}")

print("\n--- Demo Complete ---")
