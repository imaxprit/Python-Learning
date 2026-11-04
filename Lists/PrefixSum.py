# Exercise 40. Calculate Cumulative Sum (Prefix Sums)

def cumulative_sum(nums):
    total = 0
    sums = []
    for n in nums:
        total += n
        sums.append(total)
    return sums

# Test the function
numbers = [10, 20, 30, 40]
result = cumulative_sum(numbers)

print(f"Original: {numbers}")
print(f"Cumulative: {result}")