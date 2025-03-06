import random

sets = {1, 5, 3, 6, 2}
sets2 = {100}

sets.add(random.randint(1,10))
sets.add(random.randint(1,10))
sets.discard(2)

# sets cant do that

sets.update(sets2)

for h in sets:
    print(h)