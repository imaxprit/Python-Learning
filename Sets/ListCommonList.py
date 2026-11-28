# Exercise 21: Find Common Elements in Lists

list1 = [1, 2, 3, 4, 5, 3, 2]

list2 = [3, 4, 5, 6, 7, 4, 5]

common = set(list1) & set(list2)

print("common =", common)