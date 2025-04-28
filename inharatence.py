class Person():
    def __init__(self, FN, LN):
        self.FirstName = FN
        self.LastName = LN

    def printname(self):
        print(f"{self.FirstName},{self.LastName}")

class Student(Person):
    pass

person = Student("john","Dow")
person.printname()

class vihical():
    def __init__(self, B, M):
        self.Brand = B
        self.Modle = M

    def type():
        print("no type")

    def DispModle(self):
        print(f"modle: {self.Modle}, Brand: {self.Brand}")

class car(vihical):
    pass

    def move(self):
        print("Drive")

class boat(vihical):
    pass

    def move(self):
        print("sail")

class plane(vihical):
    pass

    def move(self):
        print("vroooom!!!!!")

car1 = car("germna", "fronth")
boat1 = boat("master", "bike")
plane1 = plane("bowing", "A380")

for i in (car1, boat1, plane1):
    i.move()
    i.DispModle()

class Employss:
  def __init__(self, name, salary):
    self.name = name
    self.__salary = salary

Emp = Employss("jessy", 100000)
print(f"sallery: {Emp._Employss__salary}")

class computer():
    def __init__(self):
        self.__maxPrice = 900

    def setMaxPrice(self, p):
        self.__maxPrice = p

    def sell(self):
        print(f"{self.__maxPrice}")

tomas = computer()
tomas.sell()

tomas.setMaxPrice(2000)x
tomas.sell()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"name {self.name}, age {self.age}")

p1 = person("john", 36)

print(p1)