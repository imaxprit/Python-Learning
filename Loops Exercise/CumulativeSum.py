# Exercise 27. List Cumulative Sum: Each element is the sum of all previous

mylist = [1, 2, 3, 4]
cumulative_list = []
curr_sum = 0

for num in mylist:
    curr_sum += num
    cumulative_list.append(curr_sum)


print(mylist)
print(f"Cummulative Sum:", cumulative_list)

