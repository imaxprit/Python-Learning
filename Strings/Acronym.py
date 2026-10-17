# Exercise 24. Acronym Creator

str1 = "Central Processing Unit"

# Extract the first character of each word and uppercase it
acronym = "".join([word[0].upper() for word in str1.split()])

print("Acronym:", acronym)