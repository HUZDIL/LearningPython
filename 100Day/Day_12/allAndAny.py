def All(numbers):
    for i in numbers:
        if not i:
            return False
    return True

numbers = [True,False,True,True]

print(All(numbers))

numbers = [1,2,3,4,5] #sadece sifir deger olursa false olur digerleri True deger alacaktir.

print(All(numbers))