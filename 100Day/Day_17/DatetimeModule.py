from datetime import datetime
import time

print(datetime.now())

now = datetime.now()

print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

print(datetime.ctime(now)) #daha anlasilir bir gosterim icin

print(datetime.strftime(now,"%B %Y"))

print(now.timestamp()) # su anki zamanin saniye cisinden degeri nedir?
time.sleep(2)
print(now.timestamp())

#ikitarih arasindaki zamani bulmak
tarih = datetime(1982,3,5)
tarih2 = datetime.now()
print(tarih2-tarih)