"""

      Task1_5_starter.py   -

      You may use your solution from Task1_4 if you wish instead.

      This task attempts to repeat Task1_4.py but uses a list
      comprehension instead.

"""

import glob
import os
import os.path
import glob
import os
import os.path
path = input("What is the path you would like to search?")

dir_contents = glob.glob(path)

files = [item for item in dir_contents if os.path.isfile(item)]

files.sort(key=lambda a: os.stat(a).st_size)
print(files)
