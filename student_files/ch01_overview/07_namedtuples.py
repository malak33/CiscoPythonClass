from collections import namedtuple

Contact = namedtuple('ContactRecord', 'first last age email')

records = [
    Contact('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    Contact('Ellen', 'James',   32, 'jamestel@google.com'),
    Contact('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    Contact('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]
records.sort(key=lambda a: a.age, reverse=True)

for record in records:
    print(record.last, record.age)
