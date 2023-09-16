import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://dblp.org/pid/07/1501.html")

soup = BeautifulSoup(url.content, "lxml")

articles = soup.find_all('cite', attrs= { "itemprop" : "headline" })

auteurs  = soup.find_all('cite',  attrs= { "class" : "data tts-content" })

dataset=[]

for article in articles:

  titre = article.find('span', attrs={"class" : "title"}).text

  année = article.find('span', attrs={'itemprop':'datePublished'}).text

  for auteur in auteurs:

    auteur = [ i.text for i in article.find_all('span', attrs={'itemprop':'name'})]

  dataset.append([titre, auteur, année])

df = pd.DataFrame(dataset, columns = ['Article','Auteurs','Année'])
df.sort_values("Année", ascending = True )

print(df)
