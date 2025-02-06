MesurmentConverstios = int(input("what mesurment to convert (1) leanth (2) tempture (3) weight: "))
Valid = True

if MesurmentConverstios == 1:
    leanth = int(input("leath 1: "))
    StartingLeanth = leanth
    unit1 = input("current unit (KM M CM MM MCM NM ML Y F I NM): ")
    unit2 = input("conversion unit (KM M CM MM MCM NM ML Y F I NM): ") 
    if unit1 == "KM":
        leanth=leanth
    elif unit1 == "M":
        leanth = leanth/1000
    elif unit1 == "CM":
        leanth = leanth/100000
    elif unit1 == "MM":
        leanth = leanth/1e+6
    elif unit1 == "MCM":
        leanth = leanth/1e+9
    elif unit1 == "NM":
        leanth = leanth/1e+12
    elif unit1 == "ML":
        leanth = leanth*1609
    elif unit1 == "Y":
        leanth = leanth/1094
    elif unit1 == "F":
        leanth = leanth/3281
    elif unit1 == "I":
        leanth = leanth/39370
    elif unit1 == "NM":
        leanth = leanth*1853
    else:
        print("INVALID CURRENT UNIT: " + unit1)
        Valid=False

    if unit2 == "KM":
        leanth=leanth
    elif unit2 == "M":
        leanth=leanth*1000
    elif unit2 == "CM":
        leanth=leanth*100000
    elif unit2 == "MM":
        leanth = leanth*1e+6
    elif unit2 == "MCM":
        leanth = leanth*1e+9
    elif unit2 == "NM":
        leanth = leanth*1e+12
    elif unit2 == "ML":
        leanth = leanth/1609
    elif unit2 == "Y":
        leanth = leanth*1094
    elif unit2 == "F":
        leanth = leanth*3281
    elif unit2 == "I":
        leanth = leanth*39370
    elif unit2 == "NM":
        leanth = leanth/1852
    else:
        print("INVALID CONVERSION UNIT: " + unit2)
        Valid=False
    if Valid==True:
        print("the starting leanth is: "+str(StartingLeanth), unit1 + " and has changed to: "+ str(leanth), unit2)

elif MesurmentConverstios == 2:
    temp = int(input("temputre 1: "))
    StartingTemp = temp
    unit1 = input("current unit (K F C): ")
    unit2 = input("conversion unit (K F C): ")
    if unit1 == "C":
        temp=temp
    elif unit1 == "K":
        temp = temp - 273.15
    elif unit1 == "F":
        temp = (temp - 32)*(5/9)
    else:
        print("INVALID CURRENT UNIT: " + unit1)
        Valid=False

    if unit2 == "C":
        temp=temp
    elif unit2 == "K":
        temp = temp + 273.15
    elif unit2 == "F":
        temp = (temp - 5/9)+32
    else:
        print("INVALID CONVERSION UNIT: " + unit2)
        Valid=False
    if Valid == True:
        print("the starting tempture is: "+str(StartingTemp), unit1 + " and has changed to: "+ str(temp), unit2)

elif MesurmentConverstios == 3:
    weight = int(input("weight 1: "))
    Startingweight = weight
    unit1 = input("current unit (T KG G MG MIG IT UST S P O): ")
    unit2 = input("conversion unit (T KG G MG MIG IT UST S P O): ")
    if unit1 == "KG":
        weight=weight
    elif unit1 == "T":
        weight = weight*1000
    elif unit1 == "G":
        weight = weight/1000
    elif unit1 == "MG":
        weight = weight/1e+6
    elif unit1 == "MIG":
        weight=weight/1e+9
    elif unit1 == "IT":
        weight=weight*1016
    elif unit1 == "UST":
        weight=weight*907.2
    elif unit1 == "S":
        weight=weight*6.35
    elif unit1 == "P":
        weight=weight/2.205
    elif unit1 == "O":
        weight=weight/35274
    else:
        print("INVALID CURRENT UNIT: " + unit1)
        Valid=False

    if unit2 == "KG":
        weight=weight
    elif unit2 == "T":
        weight = weight/1000
    elif unit2 == "G":
        weight = weight*1000
    elif unit2 == "MG":
        weight = weight*1e+6
    elif unit2 == "MIG":
        weight=weight*1e+9
    elif unit2 == "IT":
        weight=weight/1016
    elif unit2 == "UST":
        weight=weight/907.2
    elif unit2 == "S":
        weight=weight/6.35
    elif unit2 == "P":
        weight=weight*2.205
    elif unit2 == "O":
        weight=weight*35274
    else:
        print("INVALID CONVERSION UNIT: " + unit2)
        Valid=False
    if Valid == True:
        print("the starting weight is: "+str(Startingweight), unit1 + " and has changed to: "+ str(weight), unit2)