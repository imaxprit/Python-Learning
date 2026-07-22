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

print_range(10)
    
     