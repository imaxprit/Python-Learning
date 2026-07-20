# 1. Create a string made of the first, middle, and last character

str1 = "James"

print(str1)

first_char = str1[0]

res = len(str1)
mid_idx = int(res/2)
mid_char = str1[mid_idx]

last_char = str1[-1]

res_str = first_char + mid_char + last_char
print("New String: ",res_str)

