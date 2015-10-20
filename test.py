import sys
print ( ' IAMA Program ask me AA')
print(sys.argv[0])
print(sys.argv[1:])
a = 2
b =2
c = a + b
print(c)
d = a + b + c
print(d)



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
