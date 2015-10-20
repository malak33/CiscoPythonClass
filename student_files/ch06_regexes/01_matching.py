import re

def match_search(regex, search_str):
    if re.match(regex, search_str):
        print('begins with {0}'.format(regex))
    else:
        print('{0} not found at beginning'.format(regex))

    if re.search(regex, search_str):
        print('contains {0}'.format(regex))
    else:
        print('{0} not found within'.format(regex))


# speech refers to gettysburg address, "Four score and seven years ago, ..."
speech = open('../resources/gettysburg.txt').read()
match_search('seven', speech)
match_search('four', speech)
match_search('Four', speech)

matchobj = re.search('seven', speech)
if matchobj:
    print('seven found at position: {0}'.format(matchobj.start()))




matchobj = re.search(r'(\w+) (\w+) (\w+)', 'Four score and seven years ago')
print(matchobj.groups())                # ('Four', 'score', 'and')
print(matchobj.group(0))                # Four score and
print(matchobj.group(1))                # Four
print(matchobj.group(2))                # score
print(matchobj.group(3))                # and

str_matches = re.findall(r'\w+', 'Four score and seven years ago')
print('How many words: {0}'.format(len(str_matches)))
print(str_matches)