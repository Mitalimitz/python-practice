# Day Name
# Task: Ask for a number from 1 to 7 and print the day's name (1 = Monday).
# Print "Invalid input" for anything else.
n = int(input("Enter the number between 1 to 7"))
if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid input")
