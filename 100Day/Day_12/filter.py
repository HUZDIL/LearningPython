#same as reduce

#true/false
#ikiye bolumden kalani sifir olanlari buluyoruz
a=filter(lambda x:x%2==0,[4,5,6,7,8,5,4,3,2,4,34,435,345,654,34,567,7])
print(list(a))

def Prime_number(x):
    i=2
    if(x ==1):
        return False
    elif(x == 2):
        return True
    else:
        while(i<x):
            if(x%i == 0):
                return False
            i += 1
        return True

print(Prime_number(17))

a=filter(Prime_number,range(1,100))
print(list(a))
