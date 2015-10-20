from collections import namedtuple
import xml.etree.cElementTree as etree
from xml.etree.cElementTree import ElementTree
from xml.etree.cElementTree import Element

Contact = namedtuple('ContactRecord', 'first last age email')

records = [
    Contact('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    Contact('Ellen', 'James',   32, 'jamestel@google.com'),
    Contact('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    Contact('Keith', 'Cramer',  29, 'kcramer@sintech.com'),
]
records.sort(key=lambda a: a.age, reverse=True)


root = Element("contacts")
tree = ElementTree(root)

for record in records:
    contact = Element('contact')
    name = Element('name')
    first = Element('first')
    last = Element('last')
    email = Element('email')
    name.set('age', str(record.age))
    # name.attrib = {'age': str(record.age)}
    # name.attrib['age'] = str(record.age)
    first.text = record.first
    last.text = record.last
    email.text = record.email
    name.append(first)
    name.append(last)
    contact.append(name)
    contact.append(email)
    root.append(contact)


tree.write('results.xml', encoding='utf8')

# the Python ElementTree and cElementTree implementations do not have a pretty-print feature
# the LXML parser does, but this solution is not using LXML
from xml.dom import minidom
xml_str = etree.tostring(root)
pretty_xml = minidom.parseString(xml_str).toprettyxml(indent='   ', encoding='utf8')
print(pretty_xml.decode())