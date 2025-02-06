num = int(input("input a number: "))

if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    if num % 2 == 0:
        print("the number is mod by 2")
    if num % 3 == 0:
        print("the numer is mod by 3")
    if num % 5 == 0:
        print("the numer is mod by 5")

num_str = str(num)

if (num_str == num_str[::-1]):
    print ("this number is a paladrome")

if num <= 100 and num >= 0:
    print("is between 1 and 100")