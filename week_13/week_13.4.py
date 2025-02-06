number = int(input("Input the number of prime numbers displayed: "))
i = 0
num = 0

while i != number: # looping how many prime number the user wants to see
    num += 1
    if num > 1: # no negitive prime numbers
        for i in range(2, (num//2)+1): # checkng if its a prime number
            if (num % i) == 0:
                break
        else: # if it is a prime number; displaying the prime number
            print (f"{num}/{i+1}")
            i += 1