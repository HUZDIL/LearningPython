#my solution
def maskify(cc):
    count = 0
    cc2 =""
    for i in cc:
        count +=1
    for i in cc:
        if (count > 4):
            i = "#"
            count -=1
            cc2 +=i
        else:
            cc2 +=i
    return cc2

cc  = "haci baba nasilsin!!"
print(maskify(cc))

#other solutions
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def maskify(cc):
    newstring = ''
    for character in cc[0:-4]:
        newstring += '#'
    for number in cc[-4:]:
        newstring += number
    return newstring


maskify=lambda s:'#'*(len(s)-4)+s[-4:]