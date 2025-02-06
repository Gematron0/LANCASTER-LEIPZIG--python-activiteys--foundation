Side1 = int(input("Triangle side 1: "))
Side2 = int(input("Triangle side 2: "))
Side3 = int(input("Triangle side 3: "))

if Side1 + Side2 > Side3 and Side2 + Side3 > Side1 and Side1 + Side3 > Side2:
    if Side1 == Side2 == Side3:
        print ("is tryangle; is equilateral")
    elif Side1 == Side2 or Side2 == Side3 or Side1 == Side3:
        print ("is tryange; is isosceles")
    else:
        print ("is tryangle; is scalene")
else:
    print ("is not a tryangle")