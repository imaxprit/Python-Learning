# Exercise 16. Check if a number is a palindrome

num = 121121
temp = num
reverse_num = 0

while num > 0 :
    lastDig = num % 10
    reverse_num = (reverse_num * 10) + lastDig
    num = num // 10

if temp == reverse_num :
    print("Given number is Palindrome")
else :
    print("Given number is not a Palindrome Number")