prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
url = input('URL: ')
domain = url

for prefix in prefixes:
    if url.startswith(prefix):
        domain = url[len(prefix):]

for suffix in suffixes:
    pos = domain.find(suffix)
    if pos != -1:
        domain = domain[:pos]

print(domain)