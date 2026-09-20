# Exercise 17. Find factorial of a number

num = 6
factorial = 1

if num < 0 :
    print("Factorial not found!")
elif num == 0 :
    print("Factorial is 1.")
else :
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial of",num,"is :",factorial)