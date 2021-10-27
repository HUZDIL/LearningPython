import numpy as np
import pandas as pd

from numpy.random import randn

print(randn(3))
print(randn(3,3))

df =pd.DataFrame(data=randn(3,3),index=["a","b","c"],columns=["c1","c2","c3"])
print(df)

print(type(df["c1"])) #kolon degerlerine gore aliyor

print(df["c1"])

print(df.loc["a"]) #index degerlerine gore alacak

print(df[["c1","c3"]])

#4.kolonu eklemek
df["c4"] = pd.Series(randn(3),["a","b","c"])

print(df)
#yeni kolon eklenecek ama bu kolon 1 , kolon2 ve kolon3 un toplami olacak

df["c5"] = df["c1"]+df["c2"]+df["c3"]

print(df)

#kolon silmek icin
df.drop("c5",axis=1,inplace=True) #inplace datayi guncellemek icin kullaniliyor
print(df)

print(df.iloc[0])

#sadece bir degeri almak icin
print(df.loc["a","c1"])
print(df.loc[["a","b"],["c1","c2"]])