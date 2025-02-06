import random # imports

score = 0 # setting the score to 0

while True: # loop indefenetly
    num1 = random.randint(1, 10) # getting a random number
    num2 = random.randint(1, 10)
    PossibleProduct = int(input(f"what is the produce between {num1}*{num2}; press 0 to exit: "))
    if PossibleProduct == 0: # exiting system
        print(f"Your final score is {score}")
        break
    if PossibleProduct == num1*num2: # checking the number if its worng; else saying its wrong
        print("correct")
        score += 1
    else:
        print("worng")