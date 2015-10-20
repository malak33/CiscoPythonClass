"""

      task4_2_starter.py    -   Inheritance

      This version of the baseball app creates a TopSalaries class
      and stores a list of Players objects.

      It assumes the student_files folder is on the PYTHONPATH


      Step 1. Open support/stats.py.  (Double-check that you are working with
              the correct file).  Beneath the Player class, creat a TopSalaries
              class, as follows:


                class TopSalaries(list):
                    def __init__(self, salaries_filename, master_filename, input_year=1985, num_records=10):
                        super().__init__()
                        salaries = []
                        players = {}


      Step 2. Move the code that previously read from the two files and created
              the players dictionary and salaries list into the constructor

              Be sure to change any references from top_sals to self now.


      Step 3. Move the print_report function into the class.  Don't forget
              the first argument should become self.  Change the iteration of
              top_sals to self instead.


      Step 4. Move the salary_sort function into the class.  Make it a
              static method.  This method will NOT have self as the first
              argument.  Also, within the constructor, where salary_sort
              is used, change it to TopSalaries.salary_sort.


      Step 5. Fix any errors and test it out.
"""
import os.path
from ch04_oo.task4_2.support.stats import get_search_year, get_record_count, retrieve_data, print_report


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
