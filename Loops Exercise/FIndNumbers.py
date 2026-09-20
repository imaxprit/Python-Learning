# Exercise 15. Find largest and smallest digit in a number

num = 12345

largest = 0
smallest = 9

while num > 0 :
    digit = num % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest :", smallest)
print("Largest:", largest)