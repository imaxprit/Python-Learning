# Exercise 19. Remove Empty Strings from a List of Strings

names = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Method: Using filter with None
# filter(None, ...) removes all "Falsy" values (empty strings, 0, None)
cleaned_names = list(filter(None, names))

print(f"Cleaned Names: {cleaned_names}")