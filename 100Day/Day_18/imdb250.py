import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
#print(response)

html_content = response.content

soup =BeautifulSoup(html_content,"html.parser")

#for i in soup.find_all("td", {"class":"titleColumn"}):
 #   print(i.text)
  #  print("###############")

Titles =soup.find_all("td", {"class":"titleColumn"})
ratings =soup.find_all("td", {"class":"ratingColumn imdbRating"})

#zip fonksiyonu ile listeleri birlestir

#for Titles , ratings in zip(Titles,ratings):
 #   print("Titles :", Titles.text)
  #  print("Ratings :",ratings.text)

#kullanicidan deger alarak bunlari siralamak

a=float(input("Enter your rating"))

for Titles , ratings in zip(Titles,ratings):
    if (float(ratings)>a):
        print("Filmin ismi : {} Filmin Ratingi : {}".format(Titles,ratings))
        print("Titles :", Titles.text)
        print("Ratings :",ratings.text)


