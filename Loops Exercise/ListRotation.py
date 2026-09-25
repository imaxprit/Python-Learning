# Exercise 32. List Rotation: Rotate elements left by k positions

nums = [1, 2, 3, 4, 5]
k = 2

for x in range(k):
    first_element = nums.pop(0)
    nums.append(first_element)

print("Rotated List:", nums)