"""
    task7_1.py      - XML and ElementTree

    This exercise adds to the earlier task4_2 exercise by
    outputting XML to a file when a salary query is performed.

"""
import os.path
from ch07_xml.solutions.support.stats import get_search_year, get_record_count, TopSalaries


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
xml_filename = 'results.xml'

salfile_fullpath = os.path.join(working_dir, salaries_filename)
mastfile_fullpath = os.path.join(working_dir, master_filename)

input_year = get_search_year()
num_records = get_record_count()

top_sals = TopSalaries(salfile_fullpath, mastfile_fullpath, input_year, num_records)
top_sals.print_report(results_filename)
top_sals.create_xml(xml_filename)
test_results(results_filename)
