import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)

print(response)

icerik =response.content
soup = BeautifulSoup(icerik,"html.parser")
#print(soup.prettify())

#print(soup.find_all("a"))

#for i in soup.find_all("a"):
 #   print(i)
  #  print("#####################")

for i in soup.find_all("a"):
    print(i.get("href"))
    print("#####################")


