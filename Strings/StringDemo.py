# creating a String

a = "Python Programming"
b = "Geeks For Geeks"
print(a)
print(b)

s = """I am Learning, Python Strings
Strings are sequence of characters 
written inside quotes"""

# print(s)

s = "ABCDEF"

# positive indexing
# print(s[0])
# print(s[4])

# negative indexing
# print(s[-3])
# print(s[-5])

# string slicing
# print(s[1:4])
# print(s[:3])
# print(s[3:])
# print(s[::-1])

# Looping through strings
t = "ACERASPIRE"
# for char in t:
#     # print(char)

# String Immutability
s = "aBCDEFGH"
s = "N" + s[1:]
# print(s)

# Deleting a String
del s
# print(s)

# Updating a String
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")

# print(s1)
# print(s2)

# Common String Methods

text = "Hollywood"
# print(text)
# print(len(text))

# print(text.lower())
# print(text.upper())

newS = "    ABC   "

# print(newS)
# print(newS.strip())

s = "Python is fun"

print(s.replace("fun", "awesome"))