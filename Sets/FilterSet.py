# Exercise 20: Filter a Set

numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}

divisible_by_3 = {x for x in numbers if x % 3 == 0}

print("divisible_by_3 =", divisible_by_3)