from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
onion_r = requests.get("https://www.theonion.com/")
onion_soup = BeautifulSoup(onion_r.content, 'html.parser')
onion_headings = onion_soup.find_all('h4')
onion_news = []
for th in onion_headings:
    onion_news.append(th.text)

cd_r = requests.get("https://www.caranddriver.com/news")
cd_soup = BeautifulSoup(cd_r.content, 'html.parser')
cd_headings = cd_soup.findAll("div", {"class": "full-item-title item-title"})
cd_headings = cd_headings[2:]
cd_news = []
for hth in cd_headings:
    cd_news.append(hth.text)

def index(req):
    return render(req, 'news/index.html', {'onion_news':onion_news, 'cd_news': cd_news})