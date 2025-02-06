def apply(func, value):
    if func == "squ":
        a = value
        print(list(a))
    else:
        c = value
        print(list(c))

b = map(lambda x: x* x, a)
d = map(lambda x: x* x* x, c)

apply("squ", 5)