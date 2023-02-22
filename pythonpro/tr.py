class no:
    def __init__(self, name,age):
        self.name = name
        self.age=age

def meth(x,y):
    sum= int(x)+int(y)
    return sum
print("The sum of tow numbers is :", meth(5,3))

p1=no("manish", 25)
i=0
while i<3:
    print(p1.name,p1.age)
    i=i+1