tempeture = float(input("what is the current tempture: "))
wetherCondition = int(input("what is the current wether conditon (1) sunny (2) rainy (3) snowy: "))

if tempeture <= 45 and tempeture >= -35:
    if wetherCondition == 3 or tempeture >= 20:
        print("you need to where winter cloves")
    elif wetherCondition == 2 or tempeture >= 25:
        print("you need to where a jacket")
    else:
        print("you can where anything")
else:
    print("temuture is to low") if tempeture <= 44 else print("temputre is to high")