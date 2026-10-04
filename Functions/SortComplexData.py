# Exercise 17. Sort Complex Data with sorted() and Lambda

students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)