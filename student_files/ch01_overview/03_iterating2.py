weekdays = [
    'Monday','Tuesday',
    'Wednesday','Thursday','Friday'
]

for idx, value in enumerate(weekdays):
    print(idx, value)

for value in reversed(weekdays):
    print(value)


fruit = ['Apple', 'Orange', 'Banana', 'Watermelon']
color = ['red', 'orange', 'yellow', 'green', 'blue']

for f, c in zip(fruit, color):
    print('The {0} is {1}'.format(f, c))
