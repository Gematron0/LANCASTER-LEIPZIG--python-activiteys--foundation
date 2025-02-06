budget = input("input your budget: (1) for low (2) for medium (3) for high: ")
IsVegan = input("input yourdiatary restrictions: (1) for vegitatiean, (2) for non vegitariean: ")
Cuisine = input("input your quisines (1) for Italian (2) for india (3) for chinese: ")

if budget == "1":
    if IsVegan == "1":
        if Cuisine == "1":
            print ("italiean fast food (111)")
        elif Cuisine == "2":
            print("indian fast food (112)")
        else:
            print("chinies fast food (113)")
    elif IsVegan == "2":
        if Cuisine == "1":
            print ("italiean vegitarian fast food (121)")
        elif Cuisine == "2":
            print("indian vegitarian fast food (122)")
        else:
            print("chinies vegitarian fast food (123)")
elif budget == "2":
    if IsVegan == "1":
        if Cuisine == "1":
            print ("italiean regular food (211)")
        elif Cuisine == "2":
            print("indian regular food (212)")
        else:
            print("chinies regular food (213)")
    elif IsVegan == "2":
        if Cuisine == "1":
            print ("italiean vegitarian regular food (221)")
        elif Cuisine == "2":
            print("indian vegitarian regular food (222)")
        else:
            print("chinies vegitarian regular food (223)")
elif budget == "3":
    if IsVegan == "1":
        if Cuisine == "1":
            print ("italiean missiulan star food (311)")
        elif Cuisine == "2":
            print("indian missiulan star food (312)")
        else:
            print("chinies missiulan star food (313)")
    elif IsVegan == "3":
        if Cuisine == "1":
            print ("italiean vegitarian missiulan star food (321)")
        elif Cuisine == "2":
            print("indian vegitarian missiulan star food (322)")
        else:
            print("chinies vegitarian missiulan star food (323)")
