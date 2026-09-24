# Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.

marks = {"Aman": 85, "Baban": 70, "Chandan": 95, "Devesh": 60} 
passing_students = {}
threshold = 75

for name, mark in marks.items():
    if mark >= threshold:
        passing_students[name] = mark

print("Passing Students:", passing_students)