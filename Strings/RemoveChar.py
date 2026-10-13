# Exercise 17. Remove all characters from a string except integers

text = "I am 05 years experience in Software Development field and my package is 25L."

print("Original String:", text)

res = "".join([item for item in text if item.isdigit()])

print("Resulting digits:", res)