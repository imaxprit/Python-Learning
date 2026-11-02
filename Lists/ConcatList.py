# Exercise 37. Concatenate Two Lists in a Specific Order

def specific_concat(list1, list2):
    # Nested list comprehension for item-wise combination
    return [x + y for x in list1 for y in list2]

# Test the function
l1 = ["Hello ", "Take "]
l2 = ["Dear", "Sir"]
res = specific_concat(l1, l2)

print(f"List 1: {l1}")
print(f"List 2: {l2}")
print(f"Combined: {res}")