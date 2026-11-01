# Exercise 35. Remove Negative Numbers In-place

def remove_negatives_inplace(lst):
    # Iterate backwards through the indices
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            del lst[i]

# Test the function
my_nums = [10, -5, 20, -1, 0, -8]
print(f"Before: {my_nums}")

remove_negatives_inplace(my_nums)
print(f"After (In-place): {my_nums}")