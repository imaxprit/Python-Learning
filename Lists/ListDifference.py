# Exercise 34. Find the Difference Between Two Lists

def get_difference(list_a, list_b):
    # Convert list_b to a set for high-performance lookups
    excluded = set(list_b)
    return [item for item in list_a if item not in excluded]

# Test the function
a = [1, 2, 3, 4, 5]
b = [2, 4, 6]
result = get_difference(a, b)

print(f"List A: {a}")
print(f"List B: {b}")
print(f"Elements in A but not B: {result}")