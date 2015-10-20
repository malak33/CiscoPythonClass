"""

       Task1_3_starter.py   -   A simple grep utility


    The following syntax should work:
        python task1_3_starter.py -d wordexpression directory
        python task1_3_starter.py wordexpression file1 file2 file3 ...


    Additional tips:
    1. The starter code below has been provided for you.  This code obtains
       a list of files to search (file_list).  Your task is to search these files.

    2. Opening/reading/writing/closing files will be discussed further later,
       so for now, to read a line from a file, use:

            for line in open(filename):
                # process line from file



    Overall your procedure should be something like this:
            - Work with file_list at the bottom of the source file
            - file_list contains the list of files to search
            - Iterate over the file_list, open each file
            - Check each line in the file for existence of the wordexpression
                Hint: consider using str.find()
            - Output a result if there is a match



"""

import sys
import os
import os.path

args = sys.argv                                                 # get command-line args
if len(args) < 3:
    print('Insufficient arguments provided. Syntax:')
    print('python task1_3.py -d wordexpression directory')
    print('python task1_3.py wordexpression file1 file2 file3 ...')
    sys.exit(42)

is_directory_search = args[1].startswith('-d')                   # was a -d supplied?
word_expression = args[1]
directory_name = ''
file_list = []

if is_directory_search:
    word_expression = args[2]
    directory_name = args[3]
    dir_contents = os.listdir(directory_name)

    for entry in dir_contents:                                  # check each item if it is a file or not
        filename = os.path.join(directory_name, entry)
        if os.path.isfile(filename):
            file_list.append(filename)                          # add only files to the file_list
else:
    file_list = args[2:]


# complete your solution here.  file_list contains a list of file names to search.
for filename in file_list:
    line_count = 0
    for line in open(filename, encoding='utf8'):
        line_count += 1
        if line.find(word_expression) is not 1:
            print('File: {0}, Line: {1}, ({2})'.format(filename, line_count, word_expression))