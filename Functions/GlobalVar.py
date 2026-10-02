# Exercise 12. Modifying Global Variables

global_var = 10

def modify_variable():
    global global_var
    global_var = 20


print("Initial:", global_var)
modify_variable()
print("Modified:", global_var)