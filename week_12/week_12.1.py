password = input("input a password: ")

if len(password) >= 7:     
    if len(password) <= 8:
        print ("you password strenth is week")
    elif len(password) <= 10:
        print ("you password strenth is medium")
    else:
        print("you password strenth is strong")
else:
    print("missing one critiria (password leangh is less then 8)")