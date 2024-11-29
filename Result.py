mark=int(input("Enter obtained mark: "))
if mark>=80:
    GPA=4.00
    gread="A+"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<80 and mark>74:
    GPA = 3.75
    gread = "A"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark < 75 and mark > 69:
    GPA = 3.50
    gread = "A-"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<70 and mark>64:
    GPA = 3.25
    gread = "B+"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<65 and mark>59:
    GPA = 3.00
    gread = "B"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<60 and mark>54:
    GPA = 2.75
    gread = "B-"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark < 55 and mark > 49:
    GPA = 2.5
    gread = "C+"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<50 and mark>44:
    GPA = 2.25
    gread = "C"
    print(f"Your GPA is {GPA} and gread is {gread}")
elif mark<45 and mark>39:
    GPA = 2.00
    gread = "C-"
    print(f"Your GPA is {GPA} and gread is {gread}")
else:
    print("You are failed")