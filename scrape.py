import requests
from bs4 import BeautifulSoup

# result = requests.get("https://caps.woking.gov.uk/online-applications/currentListResults.do?action=firstPage", verify=False)
result = requests.get("https://pythonjobs.github.io/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

results = soup.find(class_="job_list")

# print(results.prettify())

job_elements = results.find_all("div", class_="job")
# print(job_elements)


for job_element in job_elements:
    job_element, end="\n"*2


# for job_element in job_elements:
#     title_element = job_element.find("h1")
#     company_element = job_element.find("p", class_="detail")
#     print(title_element.text)
#     print(company_element.text)





# python_jobs = results.find_all(
#     "h1", string=lambda text: "python" in text.lower()
# )

# python_job_elements = [
#     h1_element.parent.parent for h1_element in python_jobs
# ]

# for job_element in python_job_elements:
#     links = job_element.find_all("a")
#     for link in links:
#         print(link.text.strip()

# print(len(python_jobs))
# print(python_jobs)

