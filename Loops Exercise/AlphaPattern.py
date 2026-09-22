# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern

rows = 5
ascii_val = 65

for i in range(rows):
    letter = chr(ascii_val + i)
    for j in range(i+1):
        print(letter, end=" ")
    print()
    