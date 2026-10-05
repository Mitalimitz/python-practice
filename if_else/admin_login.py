# Admin Login
# Task: Ask for a username. If it is "admin", ask for a password.
# Correct password "1234" -> "Welcome admin", otherwise "Wrong password".
# Any other username -> "Unknown user".

u = input("Enter username")

if u == "admin":
    p = input("Enter password")
    if p == "1234":
        print("Welcome admin")
    else:
        print("Wrong password")
else:
    print("Unknown user")
