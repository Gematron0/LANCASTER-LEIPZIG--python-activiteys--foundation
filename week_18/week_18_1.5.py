studentList = ["john","geff","gabriahl","slith","toney"]
topScorstuple = (12,55,0,86,49)
submitedTests = {True,True,False,False,True}

for x in topScorstuple:
    for y in submitedTests:
        if x <= 0 and y == False:
            print(f"{x}/{y}")

t = -1
for x in topScorstuple:
    t += 1
    if x == False:
        print(studentList[t])