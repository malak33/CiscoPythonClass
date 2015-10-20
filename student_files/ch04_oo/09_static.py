import urllib.request
from urllib.error import URLError


class Page:
    @staticmethod
    def page_load(url):

        try:
            with urllib.request.urlopen(url) as f:
                results = f.read()
        except URLError as e:
            results = 'Error: {0}'.format(e)

        return results.strip()

webpage = 'http://cisco.com'

print(Page.page_load(webpage))