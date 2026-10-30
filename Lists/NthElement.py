# Exercise 28. Extract Every Nth Element from a List


def extract_nth(lst, n):
    # Using list slicing with a step of n
    return lst[::n]

# Test the function
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n_value = 3
result = extract_nth(my_list, n_value)

print(f"Original: {my_list}")
print(f"Every {n_value}rd element: {result}")