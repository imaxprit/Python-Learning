# Exercise 7. Vowel Counter

str1 = "Hello Friends"
vowels = "aeiouAEIOU"
count = 0

for char in str1:
    if char in vowels:
        count += 1

print("Total Vowels =", count)

