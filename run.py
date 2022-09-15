import requests
from bs4 import BeautifulSoup

result = requests.get("https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM=2022-02-01&daterec_to%3APARAM=2022-09-30&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=100&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced")
src = result.content
soup = BeautifulSoup(src, 'lxml')

results = soup.find("table")

sections = results.find_all('tr')

for section in sections:
    elements = section.find_all("td", class_="address")
    elements_proposal = section.find_all("td", class_="proposal")
    print(elements)
    print(elements_proposal)






