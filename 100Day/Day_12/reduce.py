
from functools import reduce

def total (x,y):
    return x+y

reduce1=reduce(total, [3,4,5,6])
print(reduce1)

print(reduce(lambda x,y : x+y, [3,4,5,6,7] ))

#max value in the list use reduce

def max(x,y):
    if (x>y):
        return x
    else:
        return y

print(max(4,5))

print(reduce(max,[34,45,45,43,9,99]))