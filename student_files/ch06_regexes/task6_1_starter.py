"""
    task6_1_starter.py      -       Using Regexes

    You may work from this file or you may use your own solution.

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


    Step 1. Add a new parameter to the function, called airport_code.
        For example:   def find_airport(name='', country='', airport_code='', filename='../../resources/airports.dat'):


    Step 2. Within the function, if the airport_code is provided, check if it is 3-letters
            using a regex.  Hint: the proper regex is: r'^[A-Z]{3}$'


    Step 3. If the airport_code if found to be valid, read each line from
            the file and check if the code is in the IATA_FAA field.  If so,
            add the line to the results found.


    Step 4. Write new doctests to test the airport_code.  An example is provided
            for you below:

    >>> find_airport(airport_code='ORD')
    ['Chicago Ohare Intl (Chicago, United States) Abbr: ORD']

"""

import collections
import csv


def find_airport(name='', country='', filename='../../resources/airports.dat'):

    if not name and not country:
        print('Provide an airport name (name=) or country (country=)')
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