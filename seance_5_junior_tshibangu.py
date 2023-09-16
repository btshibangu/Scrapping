from bs4 import BeautifulSoup
import requests
import pandas as pd
url = requests.get('https://www.imdb.com/title/tt0944947/episodes').content

_soup = BeautifulSoup(url, 'lxml')


_get_titles = _soup.find_all('a', attrs={ 'itemprop' : 'name' })
_get_titles = [ i.text for i in _get_titles]


_ratings_parent = _soup.find_all('div', attrs= {'class' : 'ipl-rating-star small'})
_ratings = [ ]

for i in _ratings_parent:
    _ratings.append(i.find('span', attrs = {"class" : 'ipl-rating-star__rating'}).text)


data = {
    'Episode' : _get_titles,
    'Ratings' : _ratings
}

df = pd.DataFrame(data)


print(df)
print("x"*50)
# toutes les saisons
link = None
_get_title_all = []
_get_rating_all = []

for i in range(1,9):
    link = requests.get(f"https://www.imdb.com/title/tt0944947/episodes?season={i}").text
    _soup_all = BeautifulSoup(link, 'lxml')
    _get_titles_ = _soup_all.find_all('a', attrs={ 'itemprop' : 'name' })

    for x in _get_titles_:
        _get_title_all.append(x.text)


    _ratings_parent_ = _soup_all.find_all('div', attrs= {'class' : 'ipl-rating-star small'})

    for i in _ratings_parent_:
        _get_rating_all.append(i.find('span', attrs = {"class" : 'ipl-rating-star__rating'}).text)


data_all = {
    'Episode saison(1-8)' : _get_title_all,
    'Ratings saison(1-8)' : _get_rating_all
}

df_2 = pd.DataFrame(data_all)
print(df_2)
