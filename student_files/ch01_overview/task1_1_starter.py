import sys

if len(sys.argv) > 1:
    user_inputs = sys.argv[1:]
else:
    user_inputs = ['100']

for one_temp in user_inputs:
    try:
        f_temp = float(one_temp)
        c_temp = (f_temp - 32) * 5.0 / 9.0
        print('%6.1f\u00b0F  = %6.1f\u00b0C' % (f_temp, c_temp))
        print('{0:6.1f}\u00b0F  = {1:6.1f}\u00b0C'.format(f_temp, c_temp))
        print('{fahr:6.1f}\u00b0F  = {cel:6.1f}\u00b0C'
                                         .format(fahr=f_temp, cel=c_temp))
    except ValueError:
        print('{0} must be a numeric value'.format(one_temp))
