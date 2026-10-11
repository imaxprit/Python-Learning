# Exercise 16. Remove special symbols/punctuation from a string

import string

given_str = "/* Ajay is Software Developer @accenture & he is earning $400K."

print("Original String:", given_str)

new_str = ""

for char in given_str:

    if char.isalnum() or char.isspace():
        new_str += char


print("New String is:", new_str)
