# Exercise 18: Remove Items Simultaneously

items = {10, 20, 30, 40, 50, 60}

to_remove = {20, 40, 60}

removed_items = items.difference_update(to_remove)

print("items =", items)
