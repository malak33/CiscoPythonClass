"""
    task8_1.py  -   Using JSON, Soup, and HTML Parsing

    This task asks you to retrieve the JSON data at the URL provided
    in the task description in the manual.

    You should then parse the data using json.loads()
    Take note: watch for parse failures and use the suggestion in the footnotes on the task slide.
    Examine the resulting data structure and notice it is a dictionary.
    Extract the url of the first incident.
    Retrieve this page using urllib.request and parse it using BeautifulSoup.
    Display the second <p> tag from this page.
"""
import json
from bs4 import BeautifulSoup
import urllib.request

page_prefix = 'http://inciweb.nwcg.gov'

request = urllib.request.Request('http://inciweb.nwcg.gov/feeds/json/markers/')
response = urllib.request.urlopen(request)
json_str = response.read().decode()

try:
    incidents = json.loads(json_str)
except ValueError:
    json_str = ''.join(json_str.rsplit(',', maxsplit=1))            # if you arrived here, there is a trailing , at the end that needs to be removed.  This will remove it.
    incidents = json.loads(json_str)

for fire in incidents['markers']:
    print('\n{firename}'.format(firename=fire['name']))
    fire_page = page_prefix + fire['url']
    response = urllib.request.urlopen(fire_page)
    html_doc = response.read().decode()
    soup = BeautifulSoup(html_doc)
    try:
        print(soup.find_all('p')[1].strong.contents[0])                        # scraping for the second <p> on the page
    except Exception as e:
        pass        # we will suppress the exception
