money = 0 # setting up varables

while True:
    print("CHOOSE AND OPTION") # main menu
    print("1; Check ballance")
    print("2; Withdraw")
    print("3; Deposit")
    print("0; Exit")
    option = int(input("what option do you wish to choose: ")) # inputing what oiption the user wants
    if option == 0:
        print("exiting porgram")
        break
    elif option == 1:
        print(f"you have {money}$")
    elif option == 2:
        subtractAmmount = int(input("hopw mutch money to withdeaw: "))
        if money-subtractAmmount >= 0: # chekcing if the number would go below 0 if withdrawing; rejecting if that is the case
            money -= subtractAmmount
            print("updated")
        else:
            print("you have to little money")
    elif option == 3: # adding money to the system
        addAmount = int(input("How mutch money do you want to add: "))
        money += addAmount
