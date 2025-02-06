income = int(input("what is your yeary income: "))

if income <= 50000:
    income=income*0.95
elif income <= 100000:
    income=income*0.90
elif income <= 150000:
    income=income*0.85
elif income <= 200000:
    income=income*0.80
elif income <= 250000:
    income=income*0.75
elif income <= 300000:
    income=income*0.70

print("your income is now " + str(income))