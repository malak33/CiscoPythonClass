"""
    task7_1_starter.py      - XML and ElementTree

    This exercise adds to the earlier task4_2 exercise by
    outputting XML to a file when a salary query is performed.


    Step 1. Open the ch07_xml/task7_1/support/stats.py file.


    Step 2. Within the TopSalaries class, add a method called:
                def create_xml(self, filename)
            that accepts a filename and dumps the top salaries into
            the file in an XML format.


    Step 3. Use the following imports to help you:
                import xml.etree.cElementTree as etree
                from xml.etree.cElementTree import ElementTree
                from xml.etree.cElementTree import Element

    Step 4. Complete the create_xml() method, using ElementTree APIs.
            To help you get started, here is a little hint:

                root = Element("players")
                tree = ElementTree(root)

                for record in self:
                    player = Element('player')

            Be sure to write the XML results out to a file.  Use the
            pretty printing technique shown in the materials.


    Step 5. In your main driver (task7_1_starter.py, i.e. this file), make
            a call to the new XML method:  top_sals.create_xml(xml_filename)


    Step 6. Test it out!

"""
import os.path
from ch07_xml.task7_1.support.stats import get_search_year, get_record_count, TopSalaries

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

top_sals = TopSalaries(salfile_fullpath, mastfile_fullpath, input_year, num_records)
top_sals.print_report(results_filename)
test_results(results_filename)
