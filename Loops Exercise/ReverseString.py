# Exercise 11. Reverse a string using a for loop (no slicing)

original = "Python"

for c in range(len(original)-1, -1, -1):
    print(original[c], end="")


reverse_str = " "

for char in original:
    reverse_str = char + reverse_str

print()
print(original)
print(reverse_str)