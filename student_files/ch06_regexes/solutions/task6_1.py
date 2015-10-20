"""
    task6_1.py      -       Using Regexes

    This module modifies the previous one (from task5_1.py) by allowing another search argument.
    It will search the 3-letter airport code and return the matching name, city, country.  The
    airport code is referred to here as the airport_code in the function definition


    >>> find_airport()
    Provide an airport name (name=) or country (country=) or 3-ltr airport code (airport_code)
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


    Newly added doctests:
    >>> find_airport(airport_code='ORD')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']
    >>> find_airport(airport_code='ord')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']
    >>> find_airport(airport_code='abcd')
    Invalid airport code
    >>> find_airport(name='Ohare', country='United', airport_code='foo')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']
    >>> find_airport(name='Ohare', airport_code='foo')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']
    >>> find_airport(airport_code='foo')
    []
    >>> find_airport(name='Ohare', country='foo', airport_code='foo')
    []
    >>> find_airport(airport_code='123')
    Invalid airport code
"""
import collections
import csv
import re


def find_airport(name='', country='', airport_code='', filename='../../resources/airports.dat'):

    if not name and not country and not airport_code:
        print('Provide an airport name (name=) or country (country=) or 3-ltr airport code (airport_code)')
        return

    if airport_code:
        airport_code = airport_code.upper()
        if not re.match(r'^[A-Z]{3}$', airport_code):
            print('Invalid airport code')
            return


    results = []
    try:
        with open(filename, encoding='utf8') as f:
            try:
                headings = f.readline().strip()[1:].split(',')                      # [1:] is stripping the \ufeff byte order mark out.
                tuple_attributes = ' '.join([heading.strip() for heading in headings])
                Airport = collections.namedtuple('Airport', tuple_attributes)
                for row in csv.reader(f):
                    airport = Airport(*row)
                    if name and country:
                        if (name in airport.name or name in airport.city) and country in airport.country:
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport.__dict__))
                    elif airport_code and airport_code in airport.IATA_FAA:
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