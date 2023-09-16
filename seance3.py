from bs4 import BeautifulSoup
import requests
import pandas as pd

html = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html").text

soup = BeautifulSoup(html, 'lxml')

ratings = soup.find_all('td', attrs = { 'class' : 'Rating' })
percents = soup.find_all('td', attrs = { 'class' : 'CocoaPercent' })

_ratings = [ i.string.strip() for i in ratings ]
_percents = [ i.string.strip() for i in percents ]

# print(_ratings)
# print(_percents)

data = {
    _ratings[0] : _ratings[ 1 : ] ,
    "Cocoa Percent" : _percents[ 1 : ],
}

df = pd.DataFrame( data)

df["Rating"] = pd.to_numeric(df['Rating'])

df.to_csv('dodi_kabeya_seance_3.csv', sep=";", index=False)
df.to_json("dodi_kabeya_seance_3.json", orient='index')
# affiche les données dans le fichier json sous forme d'une liste contenant des minis dictionnaire avec indice
# "0":{"Rating":3.75,"Cocoa Percent":"63%"} ayant comme valeurs Rating et Cocoa Percent respectivement

# df.to_json("dodi_kabeya_seance_3.json", orient='records')
# affiche les données dans le fichier json sous forme d'une liste contenant des minis dictionnaire
# {"Rating":3.75,"Cocoa Percent":"63%"} ayant comme valeurs Rating et Cocoa Percent respectivement

# df.to_json("dodi_kabeya_seance_3.json", orient='values')
# affiche les données dans le fichier json sous forme d'une liste contenant des minis liste [3.75, 63%]
# ayant comme valeurs Rating et Cocoa Percent respectivement


# print(df)


# full contents

table = soup.find('table', attrs = { 'id': 'cacaoTable'})

tbody = table.find_all('tr')

columns = []

for i in tbody[0]:
    columns.append(" ".join(i.string.strip().split()))

body = []
for i in tbody[1: ]:
    body.append([ j.string for j in i])

df_full_table = pd.DataFrame(columns= columns, data= body)
df_full_table = df_full_table.drop(columns=[''])

print(df_full_table)
