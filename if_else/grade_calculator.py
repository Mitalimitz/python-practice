# Grade Calculator
# Task: Ask for a score from 0 to 100 and print the grade:
# 90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F

score = int(input("Enter your score: "))

if score >= 90:
    print("You scored A Grade.")
elif score >= 80:
    print("You scored B Grade.")
elif score >= 70:
    print("You scored C Grade.")
elif score >= 60:
    print("You scored D Grade.")
else:
    print("You scored F Grade.")
