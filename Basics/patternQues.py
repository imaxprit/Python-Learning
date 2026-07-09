# Pattern Printing Questions

# For n = 1
# *****

# rows = 1
# n = 5
# while rows <=5 :
#     print("*", end=" ")
#     rows += 1

# n = int(input("Enter n : "))
# for i in range(n) :
#     print("*" * 5)

# for i in range(n) :
#     for j in range(1, n+1) :
#         print(j, end=" ")
#     print()


# print star pattern

n = int(input("Enter n : "))
for i in range(1, n+1) :
    print("*" * i)
print()
