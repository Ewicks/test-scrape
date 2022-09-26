import requests
from bs4 import BeautifulSoup

baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-06-01&daterec_to%3APARAM=2022-09-30&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced')

soup = BeautifulSoup(r.content, 'lxml')

appList = soup.findAll('tr')

links = []

for section in appList: # row in the column
    for link in section.find_all('a', href=True): # each row find all a tags
        newUrl = link['href']
        detailsUrl = requests.get(newUrl)
        soup = BeautifulSoup(detailsUrl.content, 'lxml')
        detailsPageLinks = soup.find('div', id='atPubMenu')
        contactLinks = detailsPageLinks.a['href']
        # print(contactLinks)
        contactUrl = requests.get(baseurl + contactLinks)
        soup1 = BeautifulSoup(contactUrl.content, 'lxml')
        # print(soup1)
        for x in soup1:
            text = soup.find('div', id='atPubContainer')
            moretext = text.findAll('div', class_='atLeftPanel')
            print(text)

        




