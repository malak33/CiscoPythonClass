"""

      task2_2_starter.py   -   Jinja2 Templating

      Reads data from multiple files.  Determines the top salaries for
      a specified year between 1985 and 2014.

      Renders output to an HTML page using Jinja2 templating

      Salaries.csv file format:  yearID,teamID,lgID,playerID,salary
      Master.csv   file format:  playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

"""

import locale
import os.path
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound

env = Environment(loader=FileSystemLoader('./templates'))

locale.setlocale(locale.LC_ALL, '')

# Step 1.  Paste your previous solution here, or copy the above imports and
#          the env declaration into your previous solution


# Step 2.  Obtain the baseball_stats.jinja template using
#          env.get_template(filename)
#          Note: the template file can be found in the ch02_files_flow_control/templates directory


# Step 3.  Pass the top_sals (your top salaries list) into the
#          tmpl.render(records=) method
#
#          The return value from the render() will be your rendered HTML results.


# Step 4. Put proper error handling around the Jinja2 template APIs
#         (as was shown in the materials)


# Step 5.  Write the rendered results to a file.  View in a browser.
