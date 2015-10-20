a = [1, 'hello', ['up', 'down']]
b = a[:]
b[0] = 5
print(a, b)

b[2][0] = 'sideways'
print(a, b)


b = list(a)
b[2][0] = 'forward'
print(a, b)

import copy
b = copy.deepcopy(a)
b[2][0] = 'backward'
print(a, b)
