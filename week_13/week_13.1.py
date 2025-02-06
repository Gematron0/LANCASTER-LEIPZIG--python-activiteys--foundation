import random # imports

RandonNumber = random.randint(1, 100) # setting up the game
attemps = 0

while True: # looping indefenetly
    Value = int(input("input a value from 1 - 100; or press -1 to exit: ")) # checking waht number the user inputs
    if Value == -1: # leaving the game
        break

    else:
        attemps += 1 # increasing the number of atteamps the user dose
        if Value > RandonNumber: # checking if the inputed number is right or worng
            print("To high")
        elif Value < RandonNumber:
            print("To small")

        else: # if the number is correct then exiting and leaving the game
            print(f"Correct; you compleated it with {attemps} attempts")
            break