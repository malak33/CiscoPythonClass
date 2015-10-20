"""

      Task1_4_starter.py   -   File size sorter utility

      This script will prompt for a path (and/or) pattern to search.
      It should display a list of files matching that path in order of largest
      to smallest


      Additional tips:

      1. Prompt for a path to search.  Example: ./*.py

      2. Perform a glob.glob(path) which returns a list of strings that match

      3. Iterate over the results, check each result to see if it is a file.
         Hint: use os.path.isfile(filename)

      4. Create a list of files only (not sub-directories)

      5. Sort the list according to file size.  Hint: use the list.sort() or sorted()

      6. Display the list.

"""
import glob
import os
import os.path
path = input("What is the path you would like to search?")

files = glob.glob(path)
list =[]

for f in files:
      if os.path.isfile(f):
            list.append(f)

list.sort(key=lambda a: os.stat(a).st_size)
print(list)

