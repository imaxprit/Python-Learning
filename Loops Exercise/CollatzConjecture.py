# Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1

n = 5
print(n, end="")

while n != 1:
    if n%2 == 0:
        n = n // 2
    else :
        n = (3 * n) + 1
    print(f",{n}",end="")