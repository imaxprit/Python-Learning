# Exercise 25. Replace List’s Item with New Value if Found

list1 = [5, 10, 15, 20, 25]
target = 20
replacement = 200

# Locate and replace
if target in list1:
    index = list1.index(target)
    list1[index] = replacement

print(f"Modified List: {list1}")