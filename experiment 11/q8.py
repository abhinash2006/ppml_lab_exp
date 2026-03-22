#!/usr/bin/env python3
"""
Q8: Read CSV and JSON files with Pandas.
Creates sample files then reads.
"""
import pandas as pd
import json

print("=== Read CSV & JSON with Pandas ===")

# Sample CSV
csv_data = """Name,Age,City
Alice,25,NY
Bob,30,LA"""
with open("sample.csv", "w") as f:
    f.write(csv_data)

df_csv = pd.read_csv("sample.csv")
print("\nCSV Data:\n", df_csv)

# Sample JSON
json_data = {
    "employees": [
        {"name": "Charlie", "age": 35, "city": "SF"},
        {"name": "Diana", "age": 28, "city": "Chicago"}
    ]
}
with open("sample.json", "w") as f:
    json.dump(json_data, f)

# Read JSON
df_json = pd.json_normalize(json_data["employees"])
print("\nJSON Data:\n", df_json)

# Cleanup
import os
for f in ["sample.csv", "sample.json"]:
    os.remove(f)
    print(f"Removed {f}")

print("\n--- Demo Complete ---")
