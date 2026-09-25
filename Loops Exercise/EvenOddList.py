# Exercise 31. Even/Odd Segregation: Move evens to front, odds to back

original = [1, 2, 3, 4, 5, 6] 

even = []
odd = []

for n in original:
    if n%2==0 :
        even.append(n)
    else :
        odd.append(n)

result = even + odd
print("Result :", result)