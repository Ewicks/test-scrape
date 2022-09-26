import requests
from bs4 import BeautifulSoup

baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}


r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-06-01&daterec_to%3APARAM=2022-09-30&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

houselist = soup.find_all('tr')

linkslist = []

for house in houselist:
    for link in house.find_all('a', href=True):
        homepagelinks = link['href']
        linkslist.append(homepagelinks)

contactlinkslist = []

for link in linkslist:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    atags = soup.find("div", id='atPubMenu').find("a")
    print(atags['href'])

    # testing = baseurl + parturl
    # contactpageurl = requests.get(testing, headers=headers)
    # newtest = BeautifulSoup(contactpageurl.content, 'lxml')
    # print(newtest)    

# print(len(contactlinkslist))

      



