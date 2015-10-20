"""

      task5_1.py    -   Doctest Example

      This module contains a single function, find_airport() that returns either
      the 3-letter abbreviation for a city name or full airport name, or all of the airports within a country.

    >>> find_airport()
    Provide an airport name (name=) or country (country=)
    >>> find_airport('Thule')
    ['Thule Air Base (Thule, Greenland) Abbr: THU']
    >>> find_airport(name='Thule')
    ['Thule Air Base (Thule, Greenland) Abbr: THU']
    >>> find_airport(name='Thule', country='Foo')
    []
    >>> find_airport(name='Ohare', country='United')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']
    >>> find_airport(country='Tuvalu')
    ['Funafuti International (Funafuti, Tuvalu) Abbr: FUN']
    >>> find_airport(foo='bar')
    Traceback (most recent call last):
      ...
    TypeError: find_airport() got an unexpected keyword argument 'foo'


"""

import collections
import csv


def find_airport(name='', country='', filename='../../resources/airports.dat'):

    if not name and not country:
        print('Provide an airport name (name=) or country (country=)')
        return
    results = []
    try:
        with open(filename, encoding='utf-8-sig') as f:
            try:
                headings = f.readline().strip().split(',')
                tuple_attributes = ' '.join([heading.strip() for heading in headings])
                Airport = collections.namedtuple('Airport', tuple_attributes)
                for row in csv.reader(f):
                    airport = Airport(*row)
                    if name and country:
                        if (name in airport.name or name in airport.city) and country in airport.country:
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport.__dict__))
                    else:
                        if name and (name in airport.name or name in airport.city):
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport.__dict__))
                        elif country and country in airport.country:
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport.__dict__))

                return results
            except csv.Error as e:
                print('Error: {err}'.format(err=e))
    except IOError as err:
        print('Error with {fn}: {err}'.format(fn=filename, err=err))

if __name__ == "__main__":
    import doctest
    doctest.testmod()