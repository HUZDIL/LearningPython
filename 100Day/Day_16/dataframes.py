import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})

print(df)

print(df.head())

print(df["Column2"].unique())

print(df["Column2"].value_counts())

print(df[(df["Column1"] > 2) & (df["Column2"] == 300)])

def times3(x):
    return x*5

b = df["Column2"].apply(times3)
print(b)
a = df["Column2"].apply(lambda x:x*3) #2. kolondaki sayilari 3 ile carpar
print(a)

df.drop("Column1",axis = 1,inplace = True)

print(df)

print(df.sort_values("Column2"))

#pivot
df = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})

print(df)

df1 = df.pivot_table(index = "Şehir",columns ="Ay",values = "Nem")
print(df1)

df2 = df.pivot_table(index = "Ay",columns ="Şehir",values = "Nem")
print(df2)
