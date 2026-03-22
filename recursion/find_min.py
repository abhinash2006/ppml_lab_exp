def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_of_rest = find_min(lst[1:])
        return lst[0] if lst[0] < min_of_rest else min_of_rest

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"List: {numbers}")
print(f"Minimum element: {find_min(numbers)}")

