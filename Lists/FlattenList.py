# Exercise 38. Flatten Nested List (2D to 1D)

def flatten_2d(nested):
    flat_list = []
    for sublist in nested:
        # extend adds all elements of the sublist to the end of flat_list
        flat_list.extend(sublist)
    return flat_list

# Test the function
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = flatten_2d(matrix)

print(f"Original 2D: {matrix}")
print(f"Flattened 1D: {result}")