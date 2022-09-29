import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-06-01&daterec_to%3APARAM=2022-09-30&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

houselist = soup.find_all('tr')

time.sleep(10)
linkslist = []

updatehouselist = []

addresslist = []

# Get all house sections that contain keyword in a list
for house in houselist:
    if (house.find('td', string=re.compile('extension'))):
        updatehouselist.append(house)


for house in updatehouselist:
    address = house.find('td', class_='address')
    addresslist.append(address.get_text())
    for link in house.find_all('a', href=True):
        homepagelinks = link['href']
        linkslist.append(homepagelinks)

contactlinkslist = []

for link in linkslist:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    atags = soup.find('div', id='atPubMenu').find('a')
    parturl = atags['href']
    contacturl = baseurl + parturl
    contactlinkslist.append(contacturl)

time.sleep(20)
contactnameslist = []

data = []

for link in contactlinkslist:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    atags = soup.find('div', class_='atPanelContainer').find('dd').find_next('dd').contents[0]
    print(atags)
#     contactnameslist.append(atags)

# time.sleep(15)
# for i, t in enumerate(zip(addresslist, contactnameslist)):
#     it = (i, t)
#     data.append(it)

# print(data)

# dataa = []
# for i, t in zip(addresslist, contactnameslist):
#     it = ('Address:', i, '|', 'name', t)
#     dataa.append(it)


# print(dataa)