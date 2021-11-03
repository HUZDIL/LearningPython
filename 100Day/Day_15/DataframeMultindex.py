import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]
list1 =list(zip(outerIndex,innerIndex))
print(list1)


list1  = pd.MultiIndex.from_tuples(list1)
print(list1)

list2 = df = pd.DataFrame(randn(9,3),list1,columns = ["A","B","C"])
print(list2)

grup1 = df.loc["Group1"]
print(grup1)
grup2index1 =df.loc["Group1"].loc["Index1"]
print(grup2index1)

grup1index1A = df.loc["Group1"].loc["Index1"]["A"]
print(grup1index1A)
print(df.index.names)

df.index.names = ["Groups","indexes"]
print(df)

print(df.xs("Group1")) #xs fonksiyounu

print(df.xs("Index1",level = "indexes"))
