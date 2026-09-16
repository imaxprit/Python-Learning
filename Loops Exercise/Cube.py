# Exercise 6. Calculate the cube of all numbers from 1 to a given number

input_num = int(input("Enter number: "))

for i in range(1, input_num+1):
    # print("Current Number is :", i,"and the cube is",i*i*i)
    print(f"Current Number is : {i} and the cube is {i*i*i}")