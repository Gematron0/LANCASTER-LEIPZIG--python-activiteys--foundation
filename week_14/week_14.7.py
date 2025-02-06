def factorial(n):
    x=n
    while n != 1:
        n -= 1
        x *= n
    return(x)

def fibonacci(n):
    x = [1, 1]
    t = 0
    z = n
    while n != 1:
        x.append(x[t]+x[t-1])
        t += 1
        n -= 1
    num = x[z]
    return(num)

print(factorial(5))
print(fibonacci(20))