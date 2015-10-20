import json
from collections import namedtuple


# convert data (dictionary) into JSON format
obj = {'task': 'run 5 miles', 'goal': 40}
print(json.dumps(obj, indent=4))


# convert custom classes (types) into JSON format
Contact = namedtuple('ContactRecord', 'first last age email')
contact = Contact('John',  'Smith',   43, 'jsbrony@yahoo.com')
print(json.dumps(contact.__dict__, indent=4))


# convert JSON strings into Python objects (dictionaries)
new_obj = json.loads('{"first": "John","last": "Smith","age": 43,"email": "jsbrony@yahoo.com"}')
print(new_obj)


# how about objects???
class Player:
    def __init__(self, first, last, salary, year):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year

p1 = Player('John', 'Smith', 30000000, 1985)
print(json.dumps(p1, default=lambda player: player.__dict__))


# what about non-serializable fields such as birthdate???
class Player2:
    def __init__(self, first, last, salary, year, birthdate):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year
        self.birthdate = birthdate

import datetime
bd = datetime.date(1970, 10, 20)
p2 = Player2('Ed', 'Green', 22000000, 198, bd)
try:
    print(json.dumps(p2, default=lambda player: player.__dict__))
except AttributeError as err:
    print('Unable to convert object p2')


# how to fix the above failure....create an encoder class that defines how to handle certain types
class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = obj.__dict__
        except (AttributeError, TypeError):
            if isinstance(obj, datetime.date):
                result = '{0}-{1}-{2}'.format(obj.year, obj.month, obj.day)
            else:
                result = 'unable to determine'

        return result

p3 = Player2('Tom', 'Summers', 18000000, 1991, bd)
print(json.dumps(p3, cls=PlayerEncoder))