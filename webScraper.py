import requests
from bs4 import BeautifulSoup

scrapeUrl = "http://www.eloratings.net/2018_World_Cup"
scrapePage = requests.get(scrapeUrl)

soup = BeautifulSoup(scrapePage.content, 'html.parser')

print scrapePage.content
