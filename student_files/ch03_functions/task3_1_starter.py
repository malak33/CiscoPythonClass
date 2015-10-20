"""

      task3_1_starter.py   -   Modules and Functions

      This was the task2_2.py solution.
      Work from this file or replace it with your own previous solutions.

      Your task: Create functions out of the solution below and move them into
                 the task3_1_support/stats.py file.  Then import that file
                 invoking those functions within your code here.


      Step 1. Either use this file or make a copy of your task2_2.py file.
              Create functions out of the different sections.  For example,
              you may wish to create a function for each of these:
              1) reading user input
              2) retrieving data
              3) printing the output


      Step 2. Move each function into the ch03_functions/task3_1_support/stats.py file.


      Step 3. Be sure to place the student_files folder on the PYTHONPATH.


      Step 4. Properly import stats.py into this file.  Invoke the functions from that file.


      Step 5. Test your solution to ensure it works.

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
        Used for the key= parameter to sort the player-salary data by salary
        :param sal_record: string value representing a players salary
        :return: integer value for the salary
    """
    salary = 0
    try:
        salary = int(sal_record[4])
    except ValueError:
        pass

    return salary


while True:
    input_year = input('Search salaries for what year?--> ')
    try:
        input_year = int(input_year)
        break
    except ValueError:
        print('Invalid year, try again.')


num_records = 10
try:
    num_records = int(input('Number of records to retrieve (def.=10): '))
except ValueError:
    print('Retrieving 10 records.')


try:
    with open(os.path.join(working_dir, salaries_filename)) as file_sal, \
         open(os.path.join(working_dir, master_filename)) as file_mast:
        for line in file_sal:                                               # get each salary record
            sal_record = line.strip().split(',')
            try:
                record_year = int(sal_record[0])
                if record_year == input_year:
                    salaries.append(sal_record)                                     # load it into a list
            except ValueError:
                pass

        for line in file_mast:                                              # get each player record
            mast_record = line.strip().split(',')
            players[mast_record[0]] = mast_record                           # load it into a list

        salaries.sort(key=salary_sort, reverse=True)                        # sort the salary records in descending order according to salary

        for top_sal in salaries:
            year = 0
            try:
                year = int(top_sal[0])                                  # get the year for each salary record
            except ValueError:
                pass

            playerid = top_sal[3]                                       # get the player's id, salary, year
            salary = top_sal[4]
            player_data = players.get(playerid)                         # get the player's name data from the other file data structure
            if player_data:                                             # checks if the player has data in the players dictionary, if not, we ignore them
                first_name = player_data[13]
                last_name = player_data[14]
                top_sals.append([first_name, last_name, salary, year])  # create a list of the player's relevant data
                if len(top_sals) == num_records:                        # stop after 10 records
                    break
except IOError as e:
    print('Error: {0}'.format(e))


try:
    with open(results_filename, 'w', encoding='utf8') as f_out:         # write the results to a file
        f_out.write('Results\n')
        f_out.write('{0:<40} {1:<20} {2:<8}\n'.format('Name', 'Salary', 'Year'))
        for player_data in top_sals:
            name = ' '.join(player_data[0:2])
            salary = locale.currency(int(player_data[2]), grouping=True)
            year = player_data[3]
            f_out.write('{0:<40} {1:<20} {2:<8}\n'.format(name, salary, year))
except IOError as e:
    print(e)


try:
    with open(results_filename) as f_test:                              # read the results back to verify them
        for line in f_test:
            print(line.rstrip())
except IOError as e:
    print(e)