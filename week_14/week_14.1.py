def add(a, b):
    return(a + b)

def subtract(a, b):
    return(a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    return(a / b)

def main():
    while True:
        a = int(input("number 1: "))
        b = int(input("number 2: "))
        print(add(a, b))
        print(subtract(a, b))
        print(multiply(a, b))
        print(divide(a, b))

if __name__ == "__main__":
    main()

