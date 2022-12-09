import requests
from bs4 import BeautifulSoup as bs
url = "http://math.gsu.edu.tr/mezun/mezun%20sayfasi.html"
r = requests.get("http://math.gsu.edu.tr/mezun/mezun%20sayfasi.html")
soup = bs(r.content,'html.parser')
print(len(soup.find_all("div","bioCard")))
