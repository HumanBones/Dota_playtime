import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def urls():
    my_url1 = "https://steamcommunity.com/profiles/76561198073103453"
    my_url2 = "https://steamcommunity.com/profiles/76561198054776412"

    urls = [my_url1,my_url2]
    rez = []

    for url in urls:
        uClient = uReq(url)
        page_html = uClient.read()
        rez.append(game_name(page_html))
        uClient.close()
        if len(rez) > 1:
            #print(rez)
            return rez


def game_name(page_html):
    page_soup = soup(page_html, "html.parser")
    games = page_soup.findAll("div",{"class":"game_name"})
    times = page_soup.findAll("div",{"class":"game_info_details"})
    num = len(games)
    for i in range(num):
        game = games[i]
        game_text = game.text
        if game_text == "Dota 2":
            return game_time(times,i)
            # return (game_time(times,i) + ' ' + game_text)
        else:
            pass
            #print("error")


def game_time(times,i):
        time = times[i]
        time_text = time.text
        time_text_re = re.compile(r'\d*.\d{3} hrs on record')
        time_text_spl = time_text_re.finditer(time_text)
        for txt in time_text_spl:
            return (txt.group(0))

urls()
