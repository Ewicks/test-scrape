import requests
from bs4 import BeautifulSoup

r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?requesttype=parseTemplate&template=PlanningContactsTab.tmplt&Filter=^APPLICATION_NUMBER^=%272022/2360%27&appno:PARAM=2022/2360&address:PARAM=73%20Hersham%20Road%20Walton-On-Thames%20Surrey%20KT12%201LN&northing:PARAM=165441&easting:PARAM=510772')

soup = BeautifulSoup(r.content, 'lxml')

text = soup.find('div', class_='atLeftPanel')

print(text.get_text())

