# Exercise 30. Remove duplicates without set

original = [1, 2, 2, 3, 4, 4, 4, 5]

unique_list = []

for num in original:
    if num not in unique_list:
        unique_list.append(num)

print("Uniquw List:", unique_list)