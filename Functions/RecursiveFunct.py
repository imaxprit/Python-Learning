# Exercise 6. Create a Recursive Function

def recursive_sum(num):
    if num :
        return recursive_sum(num-1) + num
    else :
        return 0

res = recursive_sum(10)
print(res)