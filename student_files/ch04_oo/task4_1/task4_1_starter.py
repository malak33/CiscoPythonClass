"""

      task4_1_starter.py    -   Classes

      This version of the baseball app is the Task3_1 solution.
      Task 4_1 creates a Player class and stores a list of Players
      objects.

      It assumes the student_files folder is on the PYTHONPATH.


      Step 1. Open support/stats.py.  Create a Player class here.


      Step 2. In the Player class, define a constructor (__init__)  that
              accepts a first name, last name, salary, and year


      Step 3. Create getters for each property.  Here's a sample
              for the first name property:

                    @property
                    def first_name(self):
                        return self._first_name

              Repeat this for the remaining properties.


      Step 4. Create a setter for the salary


      Step 5. In the retrieve_data() function, replace the following line:

              top_sals.append([first_name, last_name, salary, year])

              with one that first instantiates a Player() instance and then
              adds the player instance to the top_sals list


      Step 6. Can you determine how the print_report() function needs to change?
"""

import os.path

from ch04_oo.task4_1.support.stats import get_search_year, get_record_count, retrieve_data, print_report


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
