# Exercise 13. Recursive Factorial (Non-Negative Integers)

def factorial(num) :
    if num <= 1 :
        return 1
    fact = factorial(num - 1) * num
    return fact

res = factorial(5)
print(res)