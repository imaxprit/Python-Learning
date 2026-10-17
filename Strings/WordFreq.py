# Exercise 25. Word Frequency

str1 = "apple banana apple cherry banana apple"
words = str1.lower().split()
word_count = {}

for word in words:
    # Get the current count (default to 0 if not found) and add 1
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)