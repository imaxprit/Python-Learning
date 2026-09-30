# Exercise 5. Create an Inner Function

def outer_func(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5

result = outer_func(5, 10)
print(result)