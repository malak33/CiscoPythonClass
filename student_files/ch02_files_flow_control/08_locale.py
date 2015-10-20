import locale
locale.setlocale(locale.LC_ALL, '')

print(locale.currency( 223471113.18, grouping=True))


