prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
url = input('What is the url you want to navigate to?')
domain = url

for p in prefixes:
    if url.startswith(p):
        domain = url[len(p):]

for s in suffixes:
    pos = domain.find(s)
    if pos != 1:
        domain = domain[:pos]

print(domain)
