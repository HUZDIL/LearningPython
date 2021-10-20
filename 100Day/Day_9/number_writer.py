#json.dump() and json.load()

import json

numbers =[2,3,4,5,6,7,8,9]

filename = "numbers.json"
with open(filename,'w') as f:
    json.dump(numbers,f)
#numbers.json seklinde bir dosyamis olusmus oldu

numbers =[2,3,4,5,6,7,8,9]

filename = "prg.txt"
with open(filename,'w') as f:
    json.dump(numbers,f)

filename = 'numbers.json'
with open(filename) as f:
    numbers =json.load(f)
print(numbers)




