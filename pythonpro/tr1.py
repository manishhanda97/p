class record:
    def __init__(self, studentn, grade, roll):
        self.studentn=studentn
        self.grade=grade
        self.roll=roll

    def mymet(self):
        print("The grade is :", self.grade)

class record1(record):
    def __init__(self, studentn, grade, roll):
        super().__init__(studentn,grade, roll)
        self.gender="male"
p1= record1("rahul", "A+", 28)
print(p1.studentn, p1.grade, p1.roll, p1.gender)
p1.mymet()
