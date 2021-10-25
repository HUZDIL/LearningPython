import numpy as np

arr = np.arange(1,10)
print(arr)
print(arr[4])
print(arr[1:5])
print(arr[:4])

arr[:3] = 25 #ilk uc degeri aldik onlarin yerine 25 eklemis olduk

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([2,3,4,5,6])

print(arr1 + arr2)
print(arr1 * arr2 ) # Inner Product(İç Çarpım))