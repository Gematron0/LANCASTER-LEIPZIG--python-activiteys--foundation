score = int(input("input score: "))

if score >= 0 and score <= 100:
    if score >= 90:
        print ("A")
    elif score >= 80:
        print ("B")
        if score >= 88: print ("almost an A!")
    elif score >= 70:
        print("C")
        if score >= 78: print("almost a B!")
    elif score >= 60:
        print("D")
        if score >= 68: print("almost a C!")
    else:
        print("F")
        if score >= 58: print ("almost a D!")
else:
    print("score hit upper boundry; can not validate") if score > 0 else print ("score hit lower boundry; can not validyte")