# Exercise 19: The Pop Operation

s = {100, 200, 300}

popped = s.pop()
print("Popped:", popped)

s = set()
try:
    s.pop()
except KeyError as e:
    print("Error:", e)