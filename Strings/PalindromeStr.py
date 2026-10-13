# Exercise 18. Palindrome Check

def is_Palindrome(s):

    s = s.lower()

    return s == s[::-1]

print("Given String is Palindrome?\nAns:", is_Palindrome("racecar"))
