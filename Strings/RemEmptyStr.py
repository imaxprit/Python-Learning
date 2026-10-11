# Exercise 15. Remove empty strings from a list of strings

products = ["Pencil", "", "Paper", "Eraser", "Carft", "", "Scale"]

print("Original List:", products)

new_products = list(filter(None, products))

print("After Removing empty strings:", new_products)