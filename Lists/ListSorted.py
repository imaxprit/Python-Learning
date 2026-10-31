# Exercise 32. Check if List is Sorted

def is_list_sorted(lst):
    # Check if every element is <= the next element
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Test the function
nums1 = [10, 20, 30, 40]
nums2 = [10, 20, 30, 25, 40]

print(f"{nums1} sorted? {is_list_sorted(nums1)}")
print(f"{nums2} sorted? {is_list_sorted(nums2)}")