"""

       Task1_2_starter.py


 Additional Hints:
   1. Prompt for a URL input
   2. Check if URL begins with any of the prefixes (down below) by using startswith()
      If it does, capture the remaining part of the URL using slicing
      Example:
                 value = 'hello world'
                 if value.startswith('hello')
                     remaining = value[len('hello'):]

  3. Repeat this task for the suffixes.  Consider using find() for the
     suffixes.  find() returns a -1 for items not found in the string
     For example:
                 value = 'hello world'
                 position = value.find('world')
                 remaining = value[:position]
"""

prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
url = input('What is the url you want to navigate to?')
domain = url

for p in prefixes:
    if url.startswith(p):
        domain = url[len(p):]

for s in suffixes:
    pos = domain.find(s)
    if pos != -1:
        domain = domain[:pos]

print(domain)

"""