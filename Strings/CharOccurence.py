# Exercise 14. Count occurrences of all characters within a string

text = "accuracy"

char_dict = dict()

for char in text:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print(char_dict)
        