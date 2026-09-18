# Exercise 10. Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i], end=" ")



print()

for i in reversed(list1) :
    print(i, end=" ")