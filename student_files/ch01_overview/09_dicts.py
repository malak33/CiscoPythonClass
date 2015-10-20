d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}

for item in d1:                     # iterating a dictionary returns the keys
    print(item, end=' ')
else:
    print()

for val in d1.values():             # iterating the values
    print(val, end=' ')
else:
    print()

for key, val in d1.items():         # iterating both keys and values
    print('Key: {key}, Value: {val}'.format(key=key, val=val), end=' ')
else:
    print()

print(d1.get('Green'))              # returns None
print(d1.get('Green', 'N/A'))       # returns N/A
#print(d1['Green'])                 # generates a KeyError

list1 = sorted(d1.keys())
list2 = sorted(d1.values())
print(list1, list2)

list3 = [value for (key, value) in sorted(d1.items())]
print(list3)


#--------------------------------------------------------------
# using an OrderedDict
from collections import OrderedDict

d4 = OrderedDict([('Smith', 43), ('James', 32), ('Edwards', 36), ('Cramer', 29)])
for val in d4.values():
    print(val, end=' ')
else:
    print()

d4.move_to_end('Smith')
for val in d4.values():
    print(val, end=' ')
else:
    print()


#--------------------------------------------------------------
# using a defaultdict
from collections import defaultdict
d5 = defaultdict(str)
d5['greet1'] = 'hello'
print(d5['greet1'], d5['greet2'])