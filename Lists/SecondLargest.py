# Exercise 26. Find the Second Largest Number in a List

def get_second_largest(nums):
    # Remove duplicates by converting to a set
    unique_nums = list(set(nums))
    
    if len(unique_nums) < 2:
        return None
    
    # Sort the list in descending order
    unique_nums.sort(reverse=True)
    
    # Return the second element
    return unique_nums[1]

# Test the function
numbers = [12, 35, 1, 10, 34, 1, 35]
result = get_second_largest(numbers)
print(f"List: {numbers}")
print(f"Second Largest: {result}")