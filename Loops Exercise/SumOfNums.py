# Exercise 4. Calculate the sum of all numbers from 1 to N

n = int(input("Enter value of N: "))
sum = 0

for i in range(1, n+1) :
    sum = sum + i
print("Sum is:", sum)