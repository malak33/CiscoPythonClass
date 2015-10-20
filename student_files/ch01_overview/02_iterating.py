my_list = [1, 2, 3]
my_list.append(10)
my_list.insert(1, 'hello')
print(my_list)


def process_name(name):
    print(name)

while True:
    name = input('Enter name: ')
    if not name:
        break
    process_name(name)


week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for day in week:
    if day is not 'Sun' and day is not 'Sat':
        print('Weekday: ' + day)