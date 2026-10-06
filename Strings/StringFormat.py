# Exercise 1. Create a string made of the first, middle, and last character

str = "Thomas"
print("Orginal String:", str)
# print(str[0::2])

first_char = str[0]

str_len = len(str)
mid_index = int(str_len/2)
mid_char = str[mid_index]

last_char = str[-1]

new_str = first_char + mid_char + last_char
print("New String:", new_str)

