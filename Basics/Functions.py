# Functions

def add_sum(a,b):
    print(a+b)

# add_sum(5, 1

# Calling a function
def say_hello():
    print("Hello!")

# say_hello()

# Default argument
def greet(name, message="Hello"):
    print(message, name)

# greet("Rahul", "Good Evening")

# Keyword arguments (named arguments)

def info(name, age):
    print("Hello", name, "you are", age, "years old.")

# info(name="kamal", age=45)

# Positional arguments

def square_num(x, y):
    sq_num = x ** y
    print("Square is", sq_num)

# square_num(2, 5)

# Arbitrary arguments
# Non-Keyword Variable-Length Arguments (*args)
def sum_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
result = sum_numbers(1,2,3,4)
# print(result)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key+":"+value)

# display_info(name="Shraddha", age="24", city="Delhi")

def add_nums(a:int, b:int) -> int:
    return a + b
ans = add_nums(7, 5)
print(ans)