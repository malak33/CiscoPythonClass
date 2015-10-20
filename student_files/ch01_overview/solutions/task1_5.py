"""

      Task1_5.py   -

      This solution attempts to repeat Task1_4.py but uses a list
      comprehension instead.

"""

import glob
import os
import os.path
path = input('Path pattern to search: ')        # example: *.py
dir_contents = glob.glob(path)

files = [item for item in dir_contents if os.path.isfile(item)]

files.sort(key=lambda a: os.stat(a).st_size)
print(files)