from torpy.http.requests import TorRequests
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send_request(url):
    with TorRequests() as tor_requests:
        with tor_requests.get_session() as sess:
            # print the IP address of the proxy
            print(sess.get("http://httpbin.org/ip").json())
            html_content = sess.get(url, timeout=10).text
            # your scraping code here ..


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