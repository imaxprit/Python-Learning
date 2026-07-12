# Accessing Items

# Indexing

myList = ["Dog", "Cat", "Fish"]

# print(myList)
# print(myList[0])
# print(myList[-1])
# print(myList[1:3])
# print(myList[:])
# print(myList[-2:-1])

# Adding items to a list

# myList.append("Horse")
# myList.insert(1, "Cow")

# nums = [2, 4, 6]
# myList.extend(nums)
# nums.extend(myList)
# print(myList)
# print(nums)

# Removing elements from a list

# myList.remove("Fish")
# print(myList)
# myList.pop(0)
# myList.pop(0)
# print(myList)

# Changing item in a list

myList[0] = "Elephant"
# print(myList)

myList[1:3] = ["Girraf", "Fox"]
# print(myList)

# Sorting List

nums = [1, 7, 8, 4, 6, 2, 9, 3]
nums.sort()
# print(nums)

char = ["Ball", "Ant", "Ice", "Div"]
char.sort()
# print(char)

nums.sort(reverse=True)
# print(nums)

nums.reverse()
# print(nums)

newList = [x for x in char if "a" in x]
# print(newList)

# copying a List 
list1 = ["Pen", "Pencil", "Paper"]
# print(list1)
# list2 = list1
# print(list2)
# print(list1)

# list3 = list1.copy()
# print(list3)

# Concatenation of lists

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)