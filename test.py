from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.pullandbear.com/rs/man/sale-c1030036006.html')
r.html.render()

print(r.html.html)