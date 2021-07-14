from re import finditer
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
html = req.get(url)
#pprint(html.text)
soup = bs(html.text, 'html.parser')

finedust = soup.find('div', {'class':'detail_box'})
#pprint(finedust)
details = finedust.findAll('dd')
#print(details)

finedust = details[0].find('span', {'class', 'num'}).get_text()
ultrafinedust = details[1].find('span', {'class','num'}).get_text()
ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))