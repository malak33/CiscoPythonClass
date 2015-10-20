import sys
from collections import namedtuple
from xml.etree.cElementTree import ElementTree
from xml.etree.cElementTree import ParseError


Contact = namedtuple('ContactRecord', 'first last age email')
try:
    tree = ElementTree().parse('results.xml')
except ParseError as e:
    print('Parse error: {err}'.format(err=e))
    sys.exit(42)

contacts = []

for contact in tree.getiterator('contact'):
    try:
        first = contact.find('.//first').text
        last = contact.find('.//last').text
        age = contact.find('./name').get('age')
        email = contact.find('.//email').text
        contacts.append(Contact(first, last, age, email))
    except AttributeError as e:
        print('Element error: {err}'.format(err=e))

print(contacts)