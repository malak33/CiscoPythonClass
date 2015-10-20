"""
    task8_1_starter.py  -   Using JSON, Soup, and HTML Parsing

    This task asks you to retrieve the JSON data at the URL provided
    in the task description in the manual.

    You should then parse the data using json.loads()
    Take note: watch for parse failures and use the suggestion in the footnotes on the task slide.
    Examine the resulting data structure and notice it is a dictionary.
    Extract the url of the first incident.
    Retrieve this page using urllib.request and parse it using BeautifulSoup.
    Display the second <p> tag from this page.


    Step 1. Be sure to  pip install beautifulsoup4 before proceeding


    Step 2. Use the urllib.request module as shown in the materials to make a
            request to http://inciweb.nwcg.gov/feeds/json/markers/

            This should return some JSON data.  Read the response and decode() it
            to get the JSON data as a string first.

            Test this to make sure you receive a JSON string before proceeding.


    Step 3. Convert the JSON string data to an object using json.loads()

            Note: in some cases the JSON string data is mal-formed.  It has
            a trailing comma that should not be there.  The following code
            can be placed in an except block and handles the problem:

                json_str = ''.join(json_str.rsplit(',', maxsplit=1))            # if you arrived here, there is a trailing , at the end that needs to be removed.  This will remove it.
                incidents = json.loads(json_str)

    Step 4. Iterate over the 'markers' property of the JSON object.
            Hint: incidents['markers'] is a list
            Print the name of the fire.

            Test this again before proceeding.


    Step 5. While still within the iterating loop, open the url property
            for this fire (the fire's detail page) using urllib.request.urlopen(page).
            Retrieve the page's contents and use BeautifulSoup to help
            parse it as follows:

                fire_page = page_prefix + fire['url']
                response = urllib.request.urlopen(fire_page)
                html_doc = response.read().decode()
                soup = BeautifulSoup(html_doc)


    Step 6. Find all the 'p' tags and get the contents as shown here:
                print(soup.find_all('p')[1].strong.contents[0])

"""
import json
from bs4 import BeautifulSoup
import urllib.request

page_prefix = 'http://inciweb.nwcg.gov'



