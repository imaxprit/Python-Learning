# Exercise 29. Find common elements (Intersection) using loop

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_item_list = []

for item in list_a:
    if item in list_b:
        common_item_list.append(item)

print(f"Common elements: {common_item_list}")