import requests
from bs4 import BeautifulSoup

baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}


r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-06-01&daterec_to%3APARAM=2022-09-30&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

houselist = soup.find_all('tr')

list = []

for house in houselist:
    for link in house.find_all('td', class_="address"):
        link.get_text()


propolsals = []

text = 'extension'

for house in houselist:
    for link in house.find_all('td', class_="proposal"):
        proposalText = link.get_text()
        propolsals.append(proposalText)


for i in propolsals:
    print(i(text=lambda t: "extension" in t.text)

