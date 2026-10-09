# Exercise 13. Count all letters, digits, and special symbols from a given string

user = "@thearpit#tech^2026"

count_symbs = 0
count_letters = 0
count_nums = 0

for char in user:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_nums += 1
    else:
        count_symbs += 1


print(f"Total counts of chars = {count_letters}, digits = {count_nums}, and symbols = {count_symbs}")
