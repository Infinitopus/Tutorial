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

# finding highest
l = max(T1, T2, T3, T4, T5)

# letter assignment fo highest

def give_letter_grade(l):
    if l < 40:
        GL = "F"
    elif l < 50:
        GL = "D"
    elif l < 60:
        GL = "C"
    elif l < 80:
        GL = "B"
    elif l <= 100:
        GL = "A"
    else:
        GL = "Invalid"
    print(f"The highest score is {l} with grade: {GL}")

give_letter_grade(l)
print("")

# letter for ave

def give_letter_grade2(ave):
    if ave < 40:
        GM = "F"
    elif ave < 50:
        GM = "D"
    elif ave < 60:
        GM = "C"
    elif ave < 70:
        GM = "B"
    elif ave <= 100:
        GM = "A"
    else:
        GM = "Invalid"
    print(f"The average grade is {ave} with grade: {GM}")

give_letter_grade2(ave)