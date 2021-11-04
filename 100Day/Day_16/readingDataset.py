import pandas as pd

dataset = pd.read_csv("USvideos.csv")

df = pd.DataFrame(dataset)
#print(df)

print(df.index)

newdataset1 = dataset.drop(["video_id","trending_date"],axis = 1) #bu iki kolonu siliyouz ve yeni bir data set olusturuyoruz

#yeni data seti, yeni csv dosyasina yazmak
newdataset1.to_csv("UsVideos.cvs",index=False)

#excel
excelset = pd.read_excel("excelfile.xlsx")
print(excelset)

excelset["Column5"] = [170,180,190,200] #yeni colon eklendi

excelset.to_excel("excelfilenew.xlsx")

new = pd.read_html("http://www.contextures.com/xlSampleData01.html",header = 0) #0.index deki degerleri kolona yazacak
print(new[0])
