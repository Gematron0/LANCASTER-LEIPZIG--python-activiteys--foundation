car = {
  "brand": "brand name",
  "model": "model name",
  "year": 2025
}

print(car)
print(car.get('model'))
car["year"] = 2020
print(car)
car["color"] = "red"
print(car)
car.pop('model')
print(car)
car.clear()
print(car)

keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]

together = dict(zip(keys, values))
print(together)

dict1 = {
    'Ten': 10,
    'twenty': 20,
    'thirty': 30
}
dict2 = {
    'thirty': 30,
    'fourty': 40,
    'fifty': 50
}
dict3 = {**dict1, **dict2}
print(dict3)

sampleDict = {
    "class": {
        "student": {
            "name":"mike",
            "markes": {
                "phisics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["markes"]["history"]) 

employees = ['kelly', 'emma']
defalts = {'designation': 'developer', 'salary': 80000}

thisdict = dict.fromkeys(employees, defalts)
print(thisdict)

keys = ['keys', 'salary']

Dict5 = {
    'name': 'kelly',
    'age': 25,
    'salary': 8000,
    'city': 'new york'
}

keys = ['name', 'salary']
for k in keys:
    Dict5.pop(k)
print(Dict5)