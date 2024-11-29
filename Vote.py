import re
age=int(input("Age of the person : "))
nationality=input("Nationality of the person : ")
gender=input("Gender of the person: ")
if age>=18 and re.findall("Bangladeshi" or "bd" or"BD" or"bangladeshi" or "BANGLADESHI",nationality) and re.findall("m" or "f" or "3rd",gender):
            print("The person can vote.")
else:
    print("The person can not vote.")