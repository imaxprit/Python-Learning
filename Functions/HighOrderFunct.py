# Exercise 18. Create a Higher-Order Function

def apply_operation(func, x, y) :
    return func(x, y)

def add(a, b) : return a + b
def multiply(a, b) : return a * b

res_add = apply_operation(add, 5, 3)
res_mult = apply_operation(multiply, 5, 3)

print("Addition Result:", res_add)
print("Multiplication Result:", res_mult)