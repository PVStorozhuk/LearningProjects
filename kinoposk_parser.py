import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
ratingfilm = []
        # movieName = 'Мемуары гейши'
        # movieCast = 'Роб Маршалл'
movierating = []
# importing data with cleaned titles and directors to parse over
df1 = pd.read_csv('ratings1.csv')
nor = df1.values.tolist()
# function for parsing over the url for the correct title/director pair
def getKinopoiskMovieId(movieName, movieCast):
    r = requests.get('http://www.kinopoisk.ru/s/type/film/find/"' + movieName + '"/m_act%5Bcast%5D/"' + movieCast + '"/')
    soup = BeautifulSoup(r.text, 'lxml')
# 1 possibility, when the url leads to a page with multiple movies
    try:
        rez = soup.find('div', class_="rating").get_text()
        print(rez)
        return rez
    except :
        pass
# 2 possibility, when th url leads to a movie page
    try:
        rez = soup.find('span', class_="film-rating-value").get_text()
        print(rez)
        return rez
    except:
        pass
    finally:
        pass
        # print(getKinopoiskMovieId(movieName, movieCast))
# iterating over rows in our talbe
for i in nor:
    x = getKinopoiskMovieId(str(i[0]),str(i[1]))

    ratingfilm.append([i[0],x])
    time.sleep(1)
print(ratingfilm)

dfnew = pd.DataFrame(ratingfilm, columns = ['title', 'raiting'])
# uploading the results to a csv
print(dfnew)
dfnew.to_csv('ratings3.csv',index = False)