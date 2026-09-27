# Exercise 39. flatten a nested list using loops

nested_list = [[10, 20], [30, 40], [50, 60]]
flattened = []

for sublist in nested_list:
    for items in sublist:
        flattened.append(items)

print("Flattened List:", flattened)