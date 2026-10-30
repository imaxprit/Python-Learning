# Exercise 30. Find All Common Elements Between Three Lists


def find_common(list1, list2, list3):
    # Convert lists to sets and find the intersection
    common = set(list1) & set(list2) & set(list3)
    
    # Convert back to list to match expected output format
    return list(common)

# Test the function
L1 = [1, 5, 10, 20]
L2 = [6, 7, 20, 80, 100]
L3 = [3, 4, 15, 20, 30, 70, 80]

result = find_common(L1, L2, L3)
print(f"Common elements: {result}")