from datetime import datetime
#Input birth_year, month,day
birth_year=int(input("My birth year: "))
birth_month=int(input("My birth Month: "))
birth_day=int(input("My birth day: "))
#priting my birth year, month and day
print("Birth_year, birth_month, birth_day:",birth_year,birth_month,birth_day)
#Current year, month and day calculation
current_year=datetime.now().year
current_month=datetime.now().month
current_day=datetime.now().day
#printing current year, month and day
print(f"Current date Year {current_year} Month {current_month} Day {current_day}")
#my age caculation
year=current_year-birth_year
month=current_month-birth_month
day=(current_day-birth_day)
if month<0:
    year=year-1
    month=(month+12)%12
if day<0:
    month=month-1
    day=(day+30)%30
#printing my age
print(f"My age is {year} years {month} months {day} days")