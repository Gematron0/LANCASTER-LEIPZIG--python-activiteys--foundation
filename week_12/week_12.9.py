TraficLightStatuis= float(input("what is the current traflc light status (1) red (2) yellow (3) green: "))

if TraficLightStatuis == 1:
    print("(car) stop")
    print("(pedestrians) stop")
elif TraficLightStatuis == 2:
    print("(car) go slow")
    print("(pedestrians) stop")
elif TraficLightStatuis == 3:
    print("(car) go")
    print("(pedestrians) go")