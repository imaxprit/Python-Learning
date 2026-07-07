# Take the radius from the user and display the volume of sphere

# radius = int(input("Enter radius : "))
# rad_cube = radius**3
# vol_sphere = 4/3 * 3.14 * rad_cube

# print("Volume of sphere is", round(vol_sphere, 3))

# Take the principal, rate and time from the user and display the simple interest

# p = int(input("Enter principal : "))
# r = int(input("Enter rate : "))
# t = int(input("Enter time : "))
# si = (p * r * t) / 100
# print("Simple Interest is", si)

sol_exp = 3 + 2 ** 4 / 2 * 5 - 8 // 2

# 3 + 16 / 2 * 5 - 8 // 2
# 3 + 40 - 4
# 3 + 36
# print(sol_exp)

# type casting 

num = 42
# print(type(num))
# print(type(str(num)))

name = "123"
# print(type(name))
# print(type(int(name)))

# price = 425.76
# print(type(price))
# print(type(int(price)))
# print(type(str(price)))

# Write a program to convert temperature from Celsius to Fahrenheit

# cel_temp = float(input("Enter temparture in Celcius : "))

# farhenhit = (cel_temp * 9 / 5) + 32
# print("Temparature in farhenhit is", round(farhenhit, 3))

x = 10
y = 5
# print(x > y and x < 15)

x = 5
y = "2"
# print(x + y)

sol2_exp = 8 // 3 + 4 % 2
# 2 + 2 = 4.0
# print(sol2_exp)


# Take an integer input and tell if it is positive or negative (zero not included)
# num = int(input("Enter an integer : "))
# if num > 0 :
#     print(f"{num} is Positive")
# else :
#     print(f"{num} is Negative")


#  Take a positive integer input and tell if it is even or odd
# if num > 0 :
#     if (num%2 == 0) :
#         print(f"{num} is Even Number")
#     else :
#         print(f"{num} is Odd Number")
# else :
#     print("Please enter a positive(+) number")



# If cost price and selling price of an item is input through the keyboard, write a program to determine 
# whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he 
# made or loss he incurred.

# cost_price = float(input("Enter cost price = "))
# selling_price = float(input("Enter selling price = "))

# profit = selling_price - cost_price
# profit_percentage = (profit / cost_price) * 100

# if profit > 0 :
#     print(f"Seller has made profit of {profit} units, And percentage is {round(profit_percentage, 2)}%")
# elif profit < 0 :
#     print(f"Seller has incurred loss of {profit} units, And percentage is {round(profit_percentage, 2)}%")
# else :
#     print("Neither loss or Profit")

# num = int(input("Enter a positive integer = "))

# Take positive integer input and tell if it is a four digit number or not.


# if num > 0 and (num >= 1000 and num <=9999) :
#     print(f"Entered number is a four-digit number")
# else :
#     print(f"Entered number is not a four-digit number")


#  Take positive integer input and tell if it is divisible by 5 and 3.

# if (num%5==0) and (num%3==0) :
#     print(f"{num} is divisible by 5 and 3")
# else :
#     print(f"{num} is not divisible by 5 and 3")


#  Take 3 positive integers input and print the greatest of them
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))

# if num1 > num2 and num1 > num3 :
#     print(f"{num1} is greatest of them")
# elif num2 > num3 :
#     print(f"{num2} is greatest of them")
# else :
#     print(f"{num3} is greatest of them")


# Determine whether the year is a leap year or not.
# year = int(input("Enter a year : "))

# if (year%400==0) or (year%4==0 and year%100!=0) :
#     print(year, "is a leap year")
# else :
#     print(year, "is not a leap year")


# Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15
# num = int(input("Enter a number : "))

# if num%5==0 or num%3==0 :
#     if (num%15 != 0) :
#         print(num, "is divisible by 5 or 3 but not divisible by 15")
#     else :
#         print(num, "is divisible by 5 or 3 and also divisible by 15")
# else :
#     print(num, "is not divisible by 5 or 3")


#  Take 3 positive integers input and print the greatest of them (without using multiple condition)
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))

# if num1>num2 :
#     if num1 > num3 :
#         greatest = num1
#     else :
#         greatest = num3
# else :
#     if num2 > num3 :
#         greatest = num2
#     else :
#         greatest = num3

# print(f"{greatest} is the greatest of them")



# Question: Take input percentage of a student and print the Grade according to marks:
# 1) 81-100 Very Good 
# 2) 61-80 Good 
# 3) 41-60 Average 
# 4) <=40 Fail

per = float(input("Enter percentage of Student : "))
if (per>=81 and per<=100) :
    print("Very Good")
elif (per>=61 and per<=80) :
    print("Good")
elif (per>=41 and per<=60) :
    print("Average")
else :
    print("Fail")

