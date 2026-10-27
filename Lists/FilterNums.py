# Exercise 21. List Comprehension for Filtering Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract only items that are divisible by 2
even_only = [x for x in numbers if x % 2 == 0]

print(f"Even Numbers: {even_only}")