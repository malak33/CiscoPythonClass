import datetime


now1 = datetime.datetime.now()      # current date & time
now2 = datetime.date.today()        # current date
print(now1, now2)

d = datetime.date(2009, 1, 1)
print(d.year, d.month, d.day)
print('formatted using strftime: {fmt}'.format(fmt=d.strftime('Day %d of %B, Day %j in %Y, ')))

d2 = datetime.date(2011, 6, 7)
print(d2 - d)
