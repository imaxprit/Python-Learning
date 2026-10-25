# Exercise 15. Find the Longest String in a List

words = ["PHP", "Exercises", "Backend", "Python"]

# The elegant way: find the max based on length
longest = max(words, key=len)

print(f"Longest word: {longest}")