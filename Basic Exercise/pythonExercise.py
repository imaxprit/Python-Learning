# Exercise 1. Arithmetic Product and Conditional Logic

def logic_calc(num1, num2) :
    product = num1 * num2
    if product <= 1000:
        print("The result is", product)
    else :
        print("The result is", num1+num2)

# logic_calc(20,30)
# logic_calc(40, 30)

# Exercise 2. Cumulative Sum of a Range

def print_range(num):
    prev_num = 0
    for i in range(num):
        sum = prev_num + i
        print(f"Current Number {i} Previous Number {prev_num} Sum: {sum}")
        prev_num = i

# print_range(10)

# Exercise 3. String Indexing and Even Slicing

# string_val = "pynative"
# print(string_val)

# even_word = string_val[0::2]

# for i in even_word:
#     print(i)

# Exercise 4. String Slicing and Substring Removal

def remove_chars(str_val, n):
    new_val = str_val[n:]
    print(new_val)

# remove_chars("pynative", 4)
# remove_chars("pynative", 2)

    
# Exercise 5. Variable Swapping (The In-Place Method)
a = 5
b = 10
# print(f"Before Swap : a = {a}, b = {b}")
# a, b = b, a
# print(f"After Swap : a = {a}, b = {b}")

