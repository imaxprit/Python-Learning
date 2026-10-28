# Exercise 22. Concatenate Two Lists Index-wise

list1 = ["Py", "is", "awes"]

list2 = ["thon", " ", "ome"]

result = [i + j for i, j in zip(list1, list2)]

print(f"Merged List: {result}")