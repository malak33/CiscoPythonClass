
filename, outfile = 'twain.txt', 'twain_out.txt'

try:
    with open(filename) as f_in, open(outfile, 'w') as f_out:
        for line in f_in:
            f_out.write(line)
except IOError as e:
    print(e)

with open(outfile) as f:
    print(len(f.readlines()))

