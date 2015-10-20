import locale
import math

locale.setlocale(locale.LC_ALL, '')

def convert_file_size(filesize, precision=1, override=None):
    """
            Accepts a filesize in the form of an integer or float returns
            a byte abbreviation string formatted to the largest size, for example:  \n
            convert_file_size(1200)                              = '1.2 KB'         \n
            convert_file_size(120000, 2)                         = '117.19 KB'      \n
            convert_file_size(1200000000, 0)                     = '1 GB'           \n
            convert_file_size(1234567890, 2, override='MB')      = '1,177.38 MB'    \n

    :param filesize: float or int for the size of the file in bytes
    :param precision: number of decimal places to display afterwards, def is 1
    :param override: force a specific format by passing in 'KB', 'MB', 'GB', 'TB', ...
    :return: a string for the formatted value
    """
    size_name = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    try:
        idx = 1 if filesize < 1024 else size_name.index(override) + 1
    except ValueError:
        idx = int(math.floor(math.log(filesize, 1024)))
    p = math.pow(1024, idx)
    sz_raw = filesize/p
    sz = round(sz_raw, precision)
    sz_str = locale.format('%f', sz, grouping=True).rstrip('0').rstrip('.')
    sz_fmt = '{0} {1}'.format(sz_str, size_name[idx-1])
    return sz_fmt if sz_raw > 0 else '0 B'

print(convert_file_size(12))
print(convert_file_size(1200))
print(convert_file_size(1200, 3, 'MB'))
print(convert_file_size(12000000000))
print(convert_file_size(12000000000, 2, 'TB'))
print(convert_file_size(12000000000, 2, 'KB'))

