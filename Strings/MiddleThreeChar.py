# Exercise 2. Create a string made of the middle three characters

str = "JhonDipPeta"
print("Original String:", str)

str_len = len(str)
mid_index = int(str_len/2)
mid_char  = str[mid_index - 1 : mid_index + 2]

print("Middle 3 Character String:", mid_char)