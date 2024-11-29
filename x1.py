class student:
    def __init__(self,name,ID,cgpa,dept):
        self.name=name
        self.ID=ID
        self.cgpa=cgpa
        self.dept=dept
    def get_gread(self):
        if self.cgpa==4.00:
            return 'A+'
        elif self.cgpa < 4.00 and self.cgpa >= 3.75:
            return 'A'
        elif self.cgpa<3.75 and self.cgpa>=3.50:
            return 'A-'
        elif self.cgpa<3.50 and self.cgpa>=3.25:
            return 'B+'
        elif self.cgpa < 3.25 and self.cgpa >= 3.00:
            return 'B'
        elif self.cgpa<3.00 and self.cgpa>=2.75:
            return 'B-'
        else:
            return 'C'
Junayed=student('Junayed','MA-21049',3.38,'Math')
print(Junayed.cgpa)
print(Junayed.get_gread())