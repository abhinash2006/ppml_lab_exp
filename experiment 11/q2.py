
"""
Q2: NumPy datatypes and structures.
Shows dtype specification, type conversion, structured arrays.
"""
import numpy as np

print("=== NumPy DataTypes & Structures ===")

arr = np.array([1, 2, 3])
print("Default dtype:", arr.dtype)


arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print("int32 dtype:", arr_int.dtype)
print("float64 dtype:", arr_float.dtype)

arr = np.array([1, 2, 3.5])
print("Original:", arr.dtype, arr)
arr_int = arr.astype(np.int32)
print("To int32:", arr_int.dtype, arr_int)


print("\nCommon dtypes:")
print("- int8 range: -128 to 127")
print("- uint8: 0 to 255")
print("- float32: single precision")
print("- bool: True/False")


bool_arr = np.array([True, False, True])
print("Bool array dtype:", bool_arr.dtype)


structured = np.array([(1, "Alice", 25), (2, "Bob", 30)], 
                      dtype=[("id", "i4"), ("name", "U10"), ("age", "i4")])
print("\nStructured array:")
print(structured)
print("Access by field: names =", structured["name"])
print("Bob's age: ", structured[structured["name"] == "Bob"]["age"][0])

print("\n--- Demo Complete ---")
