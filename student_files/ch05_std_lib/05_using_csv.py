import csv
airports = []
try:
    with open('../resources/airports.dat', encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                airports.append(row)
                print(row)
        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)


try:
    with open('first100.dat', 'w', encoding='utf8') as f:
        try:
            csv.writer(f).writerows(airports[1:101])
        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)