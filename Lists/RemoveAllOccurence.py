# Exercise 18. Remove All Occurrences of a Specific Item


list_v = [5, 20, 15, 20, 25, 50, 20]
target = 20

# Filter the list using a comprehension
cleaned_list = [x for x in list_v if x != target]

print(f"Cleaned List: {cleaned_list}")