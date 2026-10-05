# Event Entry
# Task: Ask for age and whether they have a ticket.
# Print "Enter" only if they are 18 or over AND have a ticket.

age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? Y or N: ").upper()

if ticket == "Y" and age >= 18:
    print("Enter")
else:
    print("No entry")
