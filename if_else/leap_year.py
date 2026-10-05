# Leap Year
# Task: Ask for a year and print whether it is a leap year.
# Rules: divisible by 4 -> leap year,
#        EXCEPT divisible by 100 -> not a leap year,
#        UNLESS also divisible by 400 -> leap year.

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year.")
        else:
            print("It's not a leap year.")
    else:
        print("It's a leap year.")
else:
    print("It's not a leap year.")
