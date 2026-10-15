# Exercise 23. Longest Word

text = "The quick brown fox jumps over the lazy dog"

word = text.split()
longest = " "

for word in word:

    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

