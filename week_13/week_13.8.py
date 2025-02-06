num = int(input("input a non negitive number: "))
factorial = 1

for i in range(1, num + 1): # calculaing the factorial
    factorial *= i

print(factorial)