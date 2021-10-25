import numpy as np

data_list = [1,2,3]

arr = np.array(data_list)

print(arr)

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)

print(arr2)

print(arr2[2,2])

arr3 = np.arange(10,20) #10 dan baslayip 19 a kadar degerlerden liste yapar
print(arr3)
arr4 = np.arange(1,111,3)
print(arr4)

arr5 = np.zeros(10)
print(arr5)

arr6 = np.zeros((3,4))
print(arr6)

arr7 = np.linspace(0,100,5) # 0 ile 100 arası değerleri 5 parçaya böler.

arr7 = np.random.randint(0,10) # 0(dahil) ile 10(hariç) arasında random int oluşturur.

arr8 = np.random.randint(1,10,5) # 1(dahil) ile 10(hariç) arasında 5 değer oluşturarak 5 değer saklayan array oluşturur.

newArray = np.random.randint(1,100,10)
newArray.max()
newArray.min()
newArray.sum()
newArray.mean()
newArray.argmin() #en kucuk elemanin indexi
newArray.argmax()#en buyuk elmenanin indeksi
