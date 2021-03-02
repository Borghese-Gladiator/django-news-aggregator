import requests
from bs4 import BeautifulSoup

onion_r = requests.get("https://www.theonion.com/")
onion_soup = BeautifulSoup(r.content, 'html5lib')

onion_headings = soup.find_all('h4')

cd_r = requests.get("https://www.caranddriver.com/news")
cd_soup = BeautifulSoup(cd_r.content, 'html5lib')
cd_headings = cd_soup.findAll("div", {"class": "full-item-title item-title"})

