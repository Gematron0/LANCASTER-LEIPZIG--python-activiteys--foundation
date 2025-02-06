import time # imports

Username = "UserName" # predetermans username and passowrd; inishilising attempts
Password = "PassWord"
Attampts = 0

while True:
    while Attampts != 3: # checking if the attempts is not 3
        GuessedUsername = input("input username: ")
        GuessedPassoword = input("input password: ")

        if GuessedUsername == Username and GuessedPassoword == Password: #checking if the password is right
            print("correct")
            break
        else: # updating attempts
            Attampts += 1
            print(f"incorrect; you have {Attampts}/3 remaining")

    if Attampts == 3: # chekcinf if the user didnt use to many attempts
        print("you have reached the max ammounts of attamps")
        time.sleep(5)
        Attampts = 0
    else:
        break