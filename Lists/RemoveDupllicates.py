# Exercise 20. Remove Duplicates from List

duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicates))

print(f"Unique List: {unique_list}")