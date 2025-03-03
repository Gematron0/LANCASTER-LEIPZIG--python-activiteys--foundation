string = "Strings"
z=0
print(string[::-1])

for i in string.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        z+=1
print(z)

if (string == string[::-1]):
    print ("this number is a paladrome")
else:
    print("this is not a palladrome")