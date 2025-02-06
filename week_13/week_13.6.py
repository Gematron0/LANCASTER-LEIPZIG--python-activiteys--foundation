import random
import time
loop = 0

while loop != 5: # chekcing if the person went into 5 diffrent maze rooms
    CorrectDoor = random.randint(1, 2) # selecing which direction is the correct door
    UserDoor = int(input("what door do you wish to enter (1 for left; 2 for right; 0 to exit): "))
    if UserDoor == 0: # exiting the maze system
        print("you decided to leave the maze; which is porbobly a good idea")
        break
    elif CorrectDoor == UserDoor: # checking if the person went the right or wrong dirrection
        loop += 1
        print("you went to the next room safely")
        if loop == 5:
            print("you won!!")
            break
    else: # punicheming user if they went the wrong way
        print("you went to the wrong door; you died; game restarting in 3 seconds")
        time.sleep(3)
        loop == 0

        

