my_str = str('Python is great!')            # using the str() class constructor

print('\u26C8')                             # using 16-bit unicode chars, note: to convert to utf-8, use: '\u26C8'.encode('utf-8')
print('\N{UMBRELLA}')                       # using named unicode


b1 = bytes([65, 66, 67])	                # holds 3 ascii byte values
print(b1, b1.decode(), type(b1))            # b'ABC'  ABC  <class 'bytes'>

b2 = b'DEF'
print(b2, b2.decode(), type(b2))            # b'DEF'  DEF  <class 'bytes'>

b3 = bytes('This is utf-8 encoded', 'utf-8')
print(b3, b3.decode(), type(b3))

b4 = bytes('This is utf-16 encoded', 'utf-16')
# print(b4.decode())                       # error, utf-8 decoder would be used
print(b4.decode('utf-16'))

print('This will be utf-16 encoded'.encode('utf-16').decode('utf-16'))


s5 = 'Python is fun'
sl1 = s5[0:4]
print(sl1)


s6 = '{lang} is over {0:0.2f} {date} old.'.format(20, date='years', lang='Python')
print(s6)


# format() examples:
print('{:>8}'.format('101.55'))                 # right-justify in a field-width of 8
print('{:-^20}'.format('hello'))                # center in a field-width of 20
