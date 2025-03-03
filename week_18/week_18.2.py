string = "I like trains!"

print(string.startswith("l"))
print(string.endswith("!"))
print(string.find("i"))

for i in string.split(" "):
    print(i)
    secstring = i.join(i)

print(secstring)

slip = "  sliifsafsd   "
print(slip.strip())