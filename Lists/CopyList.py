# Exercise 9. Create a Copy of a List

original = ["Apple", "Banana", "Cherry"]

# Create a true copy
new_copy = original.copy()

# Prove they are independent
new_copy.append("Date")

print(f"Original: {original}")
print(f"Copy: {new_copy}")