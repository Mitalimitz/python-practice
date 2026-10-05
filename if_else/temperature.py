# Temperature
# Task: Ask for a temperature. Print "Hot" if above 25,
# "Mild" if 15-25, "Cold" if below 15.

temp = int(input("Enter the temperature: "))

if temp > 25:
    print("Hot")
elif temp >= 15:
    print("Mild")
else:
    print("Cold")
