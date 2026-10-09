# Exercise 11. N-th Character Removal

text = "Amazing"

index = 2

first_part = text[:index]

last_part = text[index+1:]

res = first_part + last_part

print("After removing index", index, ":", res)