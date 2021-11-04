import numpy as np
import pandas as pd


dataset = {
        "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
        "Employee": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
        "Salary":[3000,3500,2500,4500,4000,2000]
        }

print(dataset)

df = pd.DataFrame(dataset)
print(df)

depGruoup = df.groupby("Departman") #obje olusturduk
a = depGruoup.sum()
print(a)

b =depGruoup.sum().loc["Bilişim"]
print(b)

c= df.groupby("Departman").count()
print(c)

d= averagePriceB = df.groupby("Departman").mean().loc["Bilişim"]["Salary"]
print(d)
