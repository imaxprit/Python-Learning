# Exercise 24. Add New Item After a Specified Item

list1 = [10, 20, 30, 40, 50]

target = 30

new_val = 35

index = list1.index(target)

list1.insert(index+1, new_val)

print(f"Updated List:", {list1})