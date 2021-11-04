import numpy as np
import pandas as pd

#Verileri okumak

soccer  = pd.read_csv("mls-salaries-2017.csv")
#print(soccer)

#ilk 10 veriyi okumak

print(soccer.head(n=10))

print(len((soccer.index)))

#Tum maaslarin ortalamasi/max
print(soccer["base_salary"].mean())
print(soccer["base_salary"].max())

#En yüksek tazminata sahip futbolcunun soyadını bulun
a= soccer[soccer["guaranteed_compensation"].max() == soccer["guaranteed_compensation"]]
print(a)

#"Gonzalez Pirez" isimli futbolcunun oynadığı mevkiyi bulun.

b=soccer[soccer["last_name"] == "Gonzalez Pirez"]["position"].iloc[0]
print(b)

##### Mevkilere göre futbolcuları gruplayarak mevkilerde ortalama maaşları bulun

a = soccer.groupby("position").mean()
print(a)
b =soccer.groupby("club").mean()
print(b)

##### Her mevkide kaç oyuncunun olduğunu hesaplayın
a= soccer["position"].value_counts()
print(a)

##### Her takımda kaç kişinin oynadığını hesaplayın.
a= soccer["club"].value_counts()
print(a)

##### Soyadlarının içinde "son" geçen futbolcuları bulun
def re_find(last_name):
    if "son" in last_name.lower():
        return True
    return False

a= soccer[soccer["last_name"].apply(re_find)]
print(a)
print(len(a.index))



