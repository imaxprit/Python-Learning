# Exercise 34. Display fibonacci series up to 10 terms

n_term = 10
num1, num2 = 0, 1

print("Fibonacci Series:")
for i in range(n_term):
    print(num1, end=" ")
    res = num1 + num2
    num1 = num2
    num2 = res