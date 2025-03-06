lists = [1,2,3,4,5]
tuples = (1,2,3,4,5)
sets = {1,2,3,4,5}

lists.append(6)
arr_tuple = list(tuples)
arr_tuple.append(6)
sets.add(6)

tuplethelist = tuple(lists)
setthetuple = set(tuples)
listtheset = list(sets)

print(tuplethelist.__len__())
print(setthetuple.__len__())
print(listtheset.__len__())