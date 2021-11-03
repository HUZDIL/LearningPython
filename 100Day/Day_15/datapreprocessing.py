import numpy as np
import pandas as pd

#kayip verileri duzeltmek

arr = np.array(([10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]))

df = pd.DataFrame(arr,index=["I1","I2","I3"],columns=["C1","C2","C3"])
print(df)
# dropna   bu ifade icerisinde nan olan satirlari komple siler
#print(df.dropna(axis =1)) kolona gore siliyor

#eger indexte minumum iki sayi varsa onu silme
#df.dropna(thresh=2)

df1= df.fillna(value = 1) #nan yerine 1 kooyduk

print(df1)

print(df.sum())
print(df.sum().sum())

print(df.size)
print(df.isnull().sum().sum())

def calculateMean(df):
    totalsum = df.sum().sum()
    totalnum = df.size - df.isnull().sum().sum()
    return totalsum/totalnum


df2 =df.fillna(calculateMean(df))
print(df2)

