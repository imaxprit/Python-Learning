# Exercise 7. Display numbers from a list using a loop

# Given a list of numbers, iterate through it and print numbers that satisfy these conditions:
# The number must be divisible by five.
# If the number is greater than 150, skip it and move to the next.
# If the number is greater than 500, stop the loop entirely.

numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n > 500:
        break
    if n > 150:
        continue
    if n%5 == 0:
        print(n)