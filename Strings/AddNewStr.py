# Exercise 3. Append new string in the middle of a given string

def append_middle(s1, s2) :
    print("Original String:", s1, s2)

    mi = int(len(s1) / 2)

    x = s1[:mi]
    y = s1[mi:]

    res = x + s2 + y

    print("After appending a new string in middle:", res)

append_middle("Ault", "Kelly")