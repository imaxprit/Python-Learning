# 1. Print first 10 natural numbers using while loop

# n = 1
# while n <= 10:
#     print(n, end=" ")
#     n += 1

# 2. Display numbers from -10 to -1 using for loop

# for i in range(-10, 0):
#     print(i)

# 3. Display a message “Done” after successful execution of for loop

# for i in range(0, 5):
#     print(i)
# print("Done")

# 4. Calculate the sum of all numbers from 1 to N

# n = 10
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 5. Print multiplication table of a given number

# num = int(input("Enter Table Number : "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")
# print("Table of", num, "printed.")

# 6. Calculate the cube of all numbers from 1 to a given number

# given_number = int(input("Enter number :"))
# for i in range(1, given_number+1):
#     print(f"Current Number is : {i} and the cube is {i**3}")

# 7. Display numbers from a list using a loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers :    
#     if (num > 500) :
#         break
#     if (num > 150) :
#         continue
#     if (num%5 == 0) :
#         print(num)

# 8. Count occurrences of a specific element in a list

# list1 = [10, 20, 10, 30, 40, 10, 50, 20]
# target = 20
# count = 0
# for num in list1:
#     if(target == num) :
#         count += 1
# print(f"{target} appears {count} times")

# 9. Print elements from a list present at odd index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1, len(my_list), 2) :
#         print(my_list[i], end=" ")


# 10. Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# for num in reversed(list1):
#         print(num)



# 11. Create a Function with Parameters

def demo(name, age):
    print("name =",name)
    print("age =", age)

# demo("Arpit", 25)

# 12. Variable Length of Arguments (*args)

def funct1(*args):
    print("Printing Values: ")
    for i in args:
        print(i)

# funct1(20, 40, 60)
# funct1(80, 100)



