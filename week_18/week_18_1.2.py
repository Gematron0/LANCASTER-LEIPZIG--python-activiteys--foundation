tuple = ("state1", "state2", "state3", "state4", "state5")
print(tuple[0])
print(tuple[-1])

# idk whay i shuld mentation ; but jhust place it isndie of a liust then it will allow you to modify a tulip

arr_tup = list(tuple)

for i in arr_tup:
    print(i)

tuple2 = ("state6", "state7", "state8")

tuple3 = tuple+tuple2

if "state7" in tuple3:
    print ("yes")
