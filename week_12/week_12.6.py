price = int(input("input how mutch money you spent: "))
holliday = int(input("press 1 if there is a hoolday; else press 2: "))

discount = 1

if holliday == 1:
    discount -= 0.05
    print ("you gained a 5% holliday discount")
if price >= 100:
    discount -= 0.20
    print ("you gained 20% discount")
elif price >= 50:
    discount -= 0.10
    print ("you gained 10% discount")

FinalPrice = price*discount
print(FinalPrice)