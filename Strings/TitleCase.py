# Exercise 21. Title Case Logic

str1 = "hello world from python"

# Split into words
words = str1.split()
result_words = []

for word in words:
    # Capitalize first char and add the rest
    capitalized = word[0].upper() + word[1:]
    result_words.append(capitalized)

# Join back into a sentence
res = " ".join(result_words)
print(res)