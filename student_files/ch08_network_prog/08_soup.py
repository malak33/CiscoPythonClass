import urllib.request
from bs4 import BeautifulSoup

request = urllib.request.Request('http://www.cisco.com')
response = urllib.request.urlopen(request)
html_doc = response.read().decode()
soup = BeautifulSoup(html_doc)

print(soup.title)
print(soup.find_all('h2'))