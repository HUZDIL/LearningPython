arr=[1,2,3,4,5];
brr = [1,1,2,4,5,5,6,7]

m = max(arr + brr) + 1
print(m)
list = [0 for _ in range(m)]
for i in arr:
    list[i] += 1
for i in brr:
    list[i] -= 1
print( sorted([item for item in range(len(list)) if list[item] != 0]))


