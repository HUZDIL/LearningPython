
def double(x):
    return x*2

map(double,[1,2,3,4,5,6])

print(list(map(double,[1,2,3,4,5,6])))

print1 = list(map(lambda x : x*2, (1,2,3,4,5)))
print(print1)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [7,8,9,10,11]

print2 = list(map(lambda x,y : x*y , list1,list2))
print(print2)
print3 = list(map(lambda x,y,z : x*y*z , list1,list2,list3))
print(print3)