num = input("inputer a numer: ")

if (num == num[::-1]): # check if the number is a paladrom by revercing the string
    print ("this number is a paladrome")
else:
    print("this is not a palladrome")