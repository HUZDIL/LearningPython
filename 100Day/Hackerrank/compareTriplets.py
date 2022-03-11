import math
import os
import random
import re
import sys
a = [1,2,3]
b = [4,5,6]

def compareTriplets(a, b):
    a1 = 0
    b1= 0
    for i in range(len(a)):
     if (a[i]>b[i]):
         a1 +=1
     elif (a[i]<b[i]):
         b1 +=1

    return (a1,b1)

print(compareTriplets(a,b))