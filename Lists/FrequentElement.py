# Exercise 27. Find the Most Frequent Element

def find_mode(arr):
    frequency = {}
    
    # Count occurrences of each element
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the key with the maximum value
    mode = max(frequency, key=frequency.get)
    return mode

# Test the function
data = [1, 3, 3, 2, 1, 1, 4, 3, 3]
result = find_mode(data)
print(f"List: {data}")
print(f"Mode: {result}")