# Exercise 14. Reverse an integer number

num = 76542
rev = 0

while num > 0 :
    lastDig = num %10
    rev = (rev*10) + lastDig
    num = num // 10

print(rev) 