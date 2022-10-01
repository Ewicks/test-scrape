import requests
from bs4 import BeautifulSoup
import re
import time

from torpy.http.requests import TorRequests
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0'}


def send_request(url):
    with TorRequests() as tor_requests:
        with tor_requests.get_session() as sess:
            # print the IP address of the proxy
            print(sess.get("http://httpbin.org/ip").json())
            html_content = sess.get(url, timeout=10).text


if __name__ == "__main__":
    # put some random urls
    urls = [
        "https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-09-17&daterec_to%3APARAM=2022-09-29&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced",
    ]

    for link in urls:
        try:
            send_request(link)
        except Exception as e:
            print(e)
            pass

r = requests.get('https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-09-17&daterec_to%3APARAM=2022-09-29&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

houselist = soup.find_all('tr')

time.sleep(10)
linkslist = []

updatehouselist = []

addresslist = []

# Get all house sections that contain keyword in a list
for house in houselist:
    if (house.find('td', string=re.compile('variation', flags=re.I))):
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
    contactnameslist.append(atags.get_text())

time.sleep(15)
for i, t in enumerate(zip(addresslist, contactnameslist)):
    it = (i, t)
    data.append(it)

print(data)