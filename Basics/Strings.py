# Python Strings

name = 'Arav'
message = "Good Evening"
greet = '''Hello,'''
# print(greet, name, message)

# print(name[0])
# print(name[2])
# print(name[3])
# print(name[-1])

# Traversing a string

subject = "Computer"

# print(subject)
# print(len(subject))

# Using a for loop

# for i in subject:
#     print(i, end="-")

# Using a while loop

# i = 0
# while i < len(subject) :
#     print(subject[i], end=" ")
#     i+=1

# Using list comprehension 

# charcters = [char for char in subject]
# print(charcters)

# Using Enumerate for Both Index and Character

# for index, char in enumerate(subject) :
#     print(f"Character at index {index}: {char}")

# String Length

code = "Python"
# print(len(code))

# print(code.find('x'))


# Slicing a string

# print(code[:5])
# print(code[:3])

# print(code[1:])
# print(code[2:])

# print(code[-4:-1])
# print(code[1:-1])


# Modifying Strings

text = "hello, arpit"

# print(text)
# print(text.upper())
# print(text)

text2 = "Welcome to Web Development"
# print(text2)
# print(text2.lower())

text3 = "   Programming        "
# print(text3)
# print(text3.strip())

text4 = "Indigo"
# print(text4)
# print(text4.replace('ig', 'ae'))
# print(text4)

# print(text.replace('hello', 'Thanks'))

# print(text2.split())

# print(text.capitalize())

# concatenation

str1 = "Free"
str2 = "Fire"
print(str1 + " " + str2)

name = "Parker"
city = "London"
format_str = "I am {n}, from {c}".format(n=name, c=city)
print(format_str)



