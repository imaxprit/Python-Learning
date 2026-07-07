#  Conditional Statements

# age = 21
# if age > 18 :
#     print("You ara Adult")

# marks = 35
# if marks > 50 :
#     print("Pass")
# else :
#     print("Fail")


# result = int(input("Enter your result score : "))
# if result > 85 :
#     print("You scored grade A")
# elif result > 70 :
#     print("You scored grade B")
# elif result > 55 :
#     print("You scored grade C")
# else :
#     print("better luck next time")


# Match Case

def day_example(value) :
    match value :
        case 1 :
            print("Monday")
        case 2 :
            print("Tuesday")
        case 3 :
            print("Wednesday")
        case 4 :
            print("Thursday")
        case 5 :
            print("Friday")
        case 6 :
            print("Saturday")
        case 7 :
            print("Sunday")
day_example(1)
day_example(2)
day_example(6)
day_example(3)
day_example(5)