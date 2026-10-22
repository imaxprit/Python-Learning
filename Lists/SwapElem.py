# Exercise 12. Swap Two Elements at Given Indices

list_data = [23, 65, 19, 90]
idx1, idx2 = 0, 2

print(f"Original: {list_data}")

# Pythonic swap
list_data[idx1], list_data[idx2] = list_data[idx2], list_data[idx1]

print(f"Swapped: {list_data}")