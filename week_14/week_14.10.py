def sum_all(*args):
    number = len(args)
    total = 0
    for i in args:
        total += i
    totalAvrage = total/number
    return(totalAvrage)

def convert_temperature(value, unit):
    if value == "C":
        return((unit - 32)*(5/9))
    if value == "F":
        return((unit - 5/9)+32)
    else:
        return(0)

print(sum_all(2, 5, 4, 7, 10))
print(convert_temperature("C", 50))