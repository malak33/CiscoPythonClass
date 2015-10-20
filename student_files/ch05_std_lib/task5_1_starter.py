"""

      task5_1_starter.py    -   Doctest Example

      This module contains a single function, find_airport() that returns either
      the 3-letter abbreviation for a city name or full airport name, or all of the airports within a country.


    Step 2.
        Write some doctests here.  The first one has been started for you.
        Write tests for the condition if no args are passed to find_airport().
        Write a test for an invalid country, like 'Foo'.

    >>> find_airport('Thule')
    ['Thule Air Base (Thule, Greenland) Abbr: THU']



"""

import collections
import csv


def find_airport(name='', country='', filename='../resources/airports.dat'):

    # Step 1. Remove the pass statement below.


    # Step 2. Open the file, read from it using the csv module.
    #         For each record read, determine if the name provided is
    #         in the airport name or city.  If a country is provided,
    #         determine if the name AND country are a match
    #         Hint: use the 'in' operator, as in:
    #                    if name in airport.name or name in airport.city:
    #                       results.append(record)

    pass  # remove this line before starting the lab


if __name__ == "__main__":
    import doctest
    doctest.testmod()