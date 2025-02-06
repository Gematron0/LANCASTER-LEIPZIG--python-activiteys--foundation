def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return(total)

def print_details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
        

print(sum_all(1, 4, 3, 6))

print_details(num1="5", num2="4")

