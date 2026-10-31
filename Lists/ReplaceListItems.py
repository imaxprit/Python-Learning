# Exercise 31. Filter Strings by Length in a List

def filter_by_length(strings, k):
    # Using list comprehension to filter strings
    return [s for s in strings if len(s) >= k]

# Test the function
words = ["apple", "pie", "banana", "kiwi", "pear"]
min_length = 5
result = filter_by_length(words, min_length)

print(f"Original: {words}")
print(f"Filtered (length >= {min_length}): {result}")