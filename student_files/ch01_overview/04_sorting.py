# in-place sort
items = [37, 2, 0, -14]
items.sort()
print(items)               # [-14, 0, 2, 37]


# creating a new list by sorting
new_items = sorted(items)
print(new_items)           # [-14, 0, 2, 37]


# sorts a tuple, returning a list
from time import localtime
dt = tuple(localtime())
print(dt)
dt_sorted = sorted(dt)
print('Before: {0}   After: {1}'.format(dt, dt_sorted))


# sorting in reverse (both in-place and returning a new list)
items = [37, -14, 0, 2]
items.sort(reverse=True)
new_items = sorted(items, reverse=True)
print(items, new_items)

# getting a reverse-iterator
for i in reversed(range(10)):
    print(i, end=' ')


# not the expected sort results
nums = ['13', '1', '11', '4']
nums.sort()
print(nums)                     # ['1', '11', '13', '4']


# sort() using a key
def sort_func(val):
    return int(val)
nums.sort(key=sort_func)
print(nums)                     # ['1', '4', '11', '13']


# sorted() using a key
def sort_func(val):
    return int(val)
nums2 = sorted(nums, key=sort_func)
print(nums2)                    # ['1', '4', '11', '13']

# lambda examplee
f = lambda a : a * 2
print(f(2), f('hello'))


# sorting records using a key and lambda
records = [
    ('John', 'Smith', 43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James', 32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer', 29, 'kcramer@sintech.com')
]

records.sort(key=lambda a: a[2], reverse=True)
print(records)