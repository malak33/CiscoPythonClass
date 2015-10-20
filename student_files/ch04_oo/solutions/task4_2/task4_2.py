"""
      task4_2_starter.py    -   Inheritance

      This version of the baseball app creates a TopSalaries class
      and stores a list of Players objects.

      It assumes the student_files folder is on the PYTHONPATH
"""
import os.path
from ch04_oo.solutions.task4_2.support.stats import get_search_year, get_record_count, TopSalaries

def test_results(filename):
    try:
        with open(filename) as f_test:             # read the results back to verify them
            for line in f_test:
                print(line.rstrip())
    except IOError as e:
        print(e)

working_dir = '../../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

salfile_fullpath = os.path.join(working_dir, salaries_filename)
mastfile_fullpath = os.path.join(working_dir, master_filename)

input_year = get_search_year()
num_records = get_record_count()

top_sals = TopSalaries(salfile_fullpath, mastfile_fullpath, input_year, num_records)
top_sals.print_report(results_filename)
test_results(results_filename)
