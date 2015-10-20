import urllib.request
from html.parser import HTMLParser

class PageInfo(HTMLParser):

    def __init__(self):
        super().__init__()
        self.marker = False
        self.info = []

    def handle_starttag(self, tag, attribs):
        if tag == 'h1' or tag == 'title':
            self.marker = True

    def handle_data(self, data):
        if self.marker:
            self.marker = False
            self.info.append(data)

page = PageInfo()

request = urllib.request.Request('http://www.cisco.com')
response = urllib.request.urlopen(request)
page.feed(response.read().decode())
page.close()
print('Title & <h1> info: {0}'.format(' '.join(page.info)))

