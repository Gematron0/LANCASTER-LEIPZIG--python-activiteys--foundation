def main(): # function main
    loopIndefenetly = True
    while loopIndefenetly==True:
        print("select activity (1; to 5) or press 0 to exit the program")
        ActivitySelection= int(input("which activity do you wish to do: "))
        if ActivitySelection == 1:
            activity1()
        elif ActivitySelection == 2:
            activity2()
        elif ActivitySelection == 3:
            activity3()
        elif ActivitySelection == 4:
            activity4()
        elif ActivitySelection == 5:
            activity5()
        elif ActivitySelection == 0:
            loopIndefenetly = False
        else:
            print("inpout you selected is wrong")

### activiteys ###
def activity1(): # activity 1
    name="Jonas" # String
    age="18" #Integer
    gpa="3.75" #float
    IsEnrolled=True #Boolean
    print("name " + name)
    print("age " + age)
    print("gpa " + gpa)
    IsEnrolled = str(IsEnrolled)
    print("is enrolled " + IsEnrolled)

def activity2(): # activity 2
    name = input("what is your name: ")
    food = input("what is your favorate food: ")
    age = int(input("what is your age: "))
    print("hello "+ name + "("+ age +") I also like " + food)

def activity3(): # activity 3
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    print("sum ",+  num1+num2)
    print("diffrence ",+ num1-num2)
    print("product ",+ num1*num2)
    print("quotent ",+ num1//num2)

def activity4(): # activity 4
    name = input("what is your name: ")
    age = int(input("what is your age: "))
    ageTenYear = age+10
    ageTenYear = str(ageTenYear)
    age = str(age)
    yearOfBirth = input("what is your year of birth: ")
    print("hello "+ name +" you were born in "+ yearOfBirth +" makeing you "+ age +" years old")
    print("your are in 10 years you are: "+ ageTenYear)

def activity5(): # activity 5
    feet = input("hight in feet: ")
    feet = float(feet)
    inches = feet*12
    print(inches)
    inches = float(input("hight in inches: "))
    feet = inches/12
    print(feet)

if __name__ == "__main__": # start function
    main()