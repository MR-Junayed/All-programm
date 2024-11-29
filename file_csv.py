import csv
from logging import exception

#writing in a file
with open("data.txt","w",newline='') as csv_file:
    csv_write=csv.writer(csv_file)
    csv_write.writerow(["NAME", "ID", "DEPT","SCORE"])
    csv_write.writerow(["P",112,"MATH",81])
    csv_write.writerow(["A", 12, "CSE",50])
    csv_write.writerow(["X", 102, "BGE",60])
    csv_write.writerow(["Z", 152, "ECO",89])
    csv_write.writerow(["Q", 11, "CHE", 91])
#reading from file
try:
    with open("data.txt","r")as file:
        n_file=csv.reader(file)
        for row in n_file:
            print(row)
finally:
    print("done")
try:
    with open("otput.txt","r") as csv_file:
        csv_read=csv.reader(csv_file)
        for row in csv_read:
            name, ID, DEPT, SCORE = row
            if int(SCORE)>80:
                print(f"{name} and {SCORE} and {DEPT}")

except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)