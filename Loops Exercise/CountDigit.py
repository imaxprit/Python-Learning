# Exercise 13. Count total number of digits in a number

num = 758964
count = 0

while num != 0 :
    num = num // 10
    count+=1

print("Total Digits are: ", count)
