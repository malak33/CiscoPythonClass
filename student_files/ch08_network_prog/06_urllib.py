import urllib.request
import urllib.response

url = 'http://www.yahoo.com'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
the_page = response.read()
print(the_page.decode())


#shortened version...
the_page = urllib.request.urlopen('http://www.yahoo.com').read()


from urllib.parse import urlparse
result = urlparse('https://docs.python.org/3/library/index.html')
print(result)