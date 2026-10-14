# Inputs
T1 = int(input("Enter your first test score: "))
print("")
T2 = int(input("Enter your second test score: "))
print("")
T3 = int(input("Enter your third test score: "))
print("")
T4 = int(input("Enter your fourth test score: "))
print("")
T5 = int(input("Enter your fifth test score: "))
print("")

# average
ave = (T1+T2+T3+T4+T5)/5

print(f"Your average score is {ave}")

# finding highest
l = max(T1, T2, T3, T4, T5)
print(l)
print("")

# letter assignment fo highest

def give_letter_grade(l):
    if l < 40:
        Grade_letter = "F"
    elif l < 50:
        Grade_letter = "D"
    elif l < 60:
        Grade_letter = "C"
    elif l < 80:
        Grade_letter = "B"
    elif l <= 100:
        Grade_letter = "A"
    else:
        Grade_letter = "Invalid"
    print(f"{l} - {Grade_letter}")

give_letter_grade(l)
print("")

# letter for ave

def give_letter_grade2(ave):
    if ave < 40:
        Grade_letter = "F"
    elif ave < 50:
        Grade_letter = "D"
    elif ave < 60:
        Grade_letter = "C"
    elif ave < 80:
        Grade_letter = "B"
    elif ave <= 100:
        Grade_letter = "A"
    else:
        Grade_letter = "Invalid"
    print(f"{ave} - {Grade_letter}")

give_letter_grade2(ave)