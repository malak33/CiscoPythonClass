"""

      task2_1_starter.py   -   Baseball player salaries

      Reads data from multiple files.  Determines the top salaries for
      a specified year between 1985 and 2014.

      Salaries.csv file format:  yearID,teamID,lgID,playerID,salary
      Master.csv   file format:  playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

"""

import locale
import os.path

locale.setlocale(locale.LC_ALL, '')

working_dir = '../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

input_year = 0
salaries = []
players = {}
top_sals = []

def salary_sort(sal_record):
    """
        Sorts salaries by passing in a salary record
    """
    salary = 0
    try:
        salary = int(sal_record[4])
    except ValueError:
        pass

    return salary


# Step 1. Ask user (input) to determine the year to search for.


# Step 2. Open the salary file (Salaries.csv), read records from it,
#         append to the provided salaries list any salaries that match
#         the year requested by the user


# Step 3. Read player records from the master file (Master.csv).
#         Store each record in the provided players dictionary.
#         Hint:  Use players[playerid] = player_record
#                where playerid is the first field in each record
#                      and player_record is the player's data


# Step 4. Sort the salaries list by-salary using the provided function above.
#
#         Hint: Use  salaries.sort(key=salary_sort)


# Step 5. With the salaries list sorted in order by salary, you can get the top
#         10 salaries now.  For each salary, you will need to get the playerid
#         and then use the playerid to access the dictionary to get the player's
#         first and last name


# Step 6. Print the first and last name of each player as well as the salary and year.

