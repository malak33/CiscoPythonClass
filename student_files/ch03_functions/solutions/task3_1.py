"""

      task3_1.py   -   Modules and Functions

      Modularizes the Task2_1 exercise by creating functions and Python modules.ntry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

      This solution assumes the <path>/student_files directory is on the PYTHONPATH

"""

import os.path

from ch03_functions.solutions.support.stats import get_search_year, get_record_count, retrieve_data, print_report


def test_results(filename):
    try:
        with open(filename) as f_test:             # read the results back to verify them
            for line in f_test:
                print(line.rstrip())
    except IOError as e:
        print(e)


working_dir = '../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

salfile_fullpath = os.path.join(working_dir, salaries_filename)
mastfile_fullpath = os.path.join(working_dir, master_filename)


input_year = get_search_year()
num_records = get_record_count()
top_sals = retrieve_data(salfile_fullpath, mastfile_fullpath, input_year, num_records)
print_report(results_filename, top_sals)
test_results(results_filename)
