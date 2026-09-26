# Exercise 35. Perfect number check

num = 60
divisor_sum = 0

for i in range(1, (num//2) +1):
    if num % i == 0:
        divisor_sum += i


if divisor_sum == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")