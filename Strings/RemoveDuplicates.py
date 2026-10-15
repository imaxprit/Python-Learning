# Exercise 21. Remove Duplicate Characters

str1 = "google"
seen = set()
result = []

for char in str1:
    if char not in seen:
        result.append(char)
        seen.add(char)

res_str = "".join(result)
print("Original:", str1)
print("Cleaned:", res_str)
