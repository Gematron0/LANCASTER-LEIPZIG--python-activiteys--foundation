num = int(input("starting number: "))
steps = 0

while num != 1: # calculation the two rules untill the value is equal to 1
    steps += 1
    if num % 2 == 0:
        num = num/2
    else:
        num = (num * 3) + 1

print(f"the number of steps it took is {steps}")