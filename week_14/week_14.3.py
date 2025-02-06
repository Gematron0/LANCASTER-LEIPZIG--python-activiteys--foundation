import math

def area_of_rectangle(leanth, width):
    return(leanth*width)

def circumference_of_circle(radius):
    return(2 * math.pi * radius)

def describe_circle(radius):
    return(tuple(((2 * math.pi * radius), ((math.pi * radius) * 2))))

print(area_of_rectangle(2, 4))

print(circumference_of_circle(5))

a = describe_circle(5)
print(type(a))
print(a)