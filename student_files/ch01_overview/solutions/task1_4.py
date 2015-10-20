"""

      Task1_4.py   -   File size sorter utility

      This script will prompt for a path (and/or) pattern to search.
      It displays the list of files in order of largest to smallest

"""
import glob
import os
import os.path

path = input('Path pattern to search: ')        # example: *.py
dir_contents = glob.glob(path)
files = []
for item in dir_contents:
    if os.path.isfile(item):
        files.append(item)

files.sort(key=lambda a: os.stat(a).st_size)
print(files)