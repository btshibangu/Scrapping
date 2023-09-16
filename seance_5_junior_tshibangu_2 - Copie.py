import pandas as pd
from bs4 import BeautifulSoup
import requests

noms = []
descriptions = []
prix = []

for element in range(1, 21):
    url = requests.get(f"https://www.webscraper.io/test-sites/e-commerce/static/computers/laptops?page={element}").text
    _soup = BeautifulSoup(url, 'lxml')

    _parent = _soup.find_all("div", attrs={"class": "caption"})
    for nom in _parent:
        noms.append( nom.find("a", attrs={"class": 'title'}).text )

    for description in _parent:
        descriptions.append( description.find("p", attrs={"class": 'description'}).text )

    for _prix in _parent:
        prix.append( _prix.find("h4", attrs={"class": 'pull-right price'}).text )

data = {
    "Noms" : noms,
    "Description" : descriptions,
    "Prix" : prix
}

df = pd.DataFrame(data)
print(df)
