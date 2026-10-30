# Exercise 29. Check if List is Palindrome

def is_palindrome(lst):
    # Compare the list to its reverse
    return lst == lst[::-1]

# Test cases
test1 = [1, 2, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]

print(f"{test1} is palindrome? {is_palindrome(test1)}")
print(f"{test2} is palindrome? {is_palindrome(test2)}")