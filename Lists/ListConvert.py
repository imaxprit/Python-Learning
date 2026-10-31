# Exercise 33. List to Dictionary Conversion

def lists_to_dict(keys, values):
    # Zip pairs the elements, dict() converts pairs to key-value entries
    return dict(zip(keys, values))

# Test the function
fields = ["name", "age", "city"]
data = ["Alice", 25, "New York"]
result = lists_to_dict(fields, data)

print(f"Keys: {fields}")
print(f"Values: {data}")
print(f"Resulting Dict: {result}")