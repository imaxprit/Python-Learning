# Python Collections(Arrays)

# This collection in python contains 4 built in datatypes:
# 1. Lists
# 2. Tuple
# 3. Set
# 4. Dictionary

# List

my_list = ["apple", "banana", "cherry"]
# print(my_list)

# print(my_list[0])
# print(my_list[1])
# print(my_list[-2])
# print(my_list[-1])

my_list[1] = "mango"
# print(my_list)


colors = ["Red", "Blue", "Green", "Yellow"]
# print(colors)
# print(type(colors))

num = [10, 12, 15, 18, 21]
# print(num)
# print(type(num))

result = [78.5, 89.9, 68.7, 86.4]
# print(result)

info = ["Arpit", 71, 85.7, True]
info = [14, "Harshit", 71, 85.7, 14, "Harshit"]
# print(info)
# print(info[0])

# for i in info:
#     print(i)

# print(type(info))

# print(len(info))

newList = list(("amazon", "google", "meta"))
# print(newList)
# print(type(newList))

# taking input for a list:

# this_list = []
# n = 4
# for i in range(n) :
#     element = int(input("enter element : "))
#     this_list.append(element)
# print(this_list)


# TUPLES

# my_tuple = ("ant","rat", "cat", "rat")
# print(my_tuple)
# print(type(my_tuple))

# print(my_tuple[0])
# my_tuple[0] = "Fish"
# print(my_tuple)

fruit = ("apple",)
# print(fruit)
# print(type(fruit))
# print(len(fruit))

# myTuple = tuple(("a",12, 75.8))
# print(myTuple)

# print(myTuple[0])
# print(myTuple[-1])

# dist = ("UP32", "UP78", "UP65", "UP25", "UP14")
# print(dist[-3:-1])

# if "UP70" in dist :
#     print("Valid")

# for x in dist :
    # print(x)

# cities = ("Lucknow", "Kanpur", "Varanasi", "Bareilly", "Noida")
# print(dist + cities)


# Sets

this_set = {"Rohn", "Peter", "Joe", "Harry", "Peter", 45, 78, 49.85}
# print(this_set)
# print(type(this_set))
# print(len(this_set))

# for x in this_set :
#     print(x)

# print("Harry" in this_set)
# this_set.add("steave")
# print(this_set)

# val = ["A", "B"]
# this_set.update(val)
# print(this_set)
# print(type(this_set))
# this_set.remove("A")
# this_set.remove("B")
# print(this_set)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)


# Dictionary

product = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red", "white", "blue"],
}

# print(product)
# print(type(product))
# print(len(product))

info = dict(name="arpit", age=22, country="India")
# print(info)
# print(type(info))

x = info.get("name")
# print(x)

y = product.keys()
# print(y)

info["name"] = "Rohan"
# print(info)
info["marks"] = 78
# print(info)

add_info = {"gender": "male"}
info.update(add_info)
# print(info)

info.pop("gender")
# print(info)

info.popitem()
# print(info)

del add_info["gender"]
# print(add_info)

info.clear()
# print(info)

items = {
    "Pencil" : 15,
    "Pen" : 25,
    "Eraser" : 10
}
# items["Pen"] = 40
# for x in items :
#     print(x)
#     # print(type(x))
#     print(items[x])
#     print(items.values())

# for x, y in items.items() :
#     print(x, y)

# items2 = items
# print(items2)

# myItems = items.copy()
# print(myItems)


# Nested Dictionaries

student = {
    "student1" : {
        "name" : "Aman",
        "age" : 21,
        "marks" : 89.85
    },
    "student2" : {
        "name" : "Rajat",
        "age" : 22,
        "marks" : 78.63
    },
    "student3" : {
        "name" : "Palak",
        "age" : 20,
        "marks" : 95.74 
    },
}

print(student)
print(type(student))

print(student["student1"]["name"])