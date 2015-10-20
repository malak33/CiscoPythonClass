import sys


def whichmod(modules):
    for module in modules:
        if module in sys.builtin_module_names:
            print('{module} built in'.format(module=module))
        else:
            try:
                module = __import__(module)
                location = module.__file__
                print('{loc}'.format(loc=location))
            except (ValueError, ImportError):
                print('{module} not found'.format(module=module))

if len(sys.argv) > 1:                                               # accept names from command-line
    modules = sys.argv[1:]
else:                                                               # or read from input
    module_names = input('Module name(s) [separated by spaces]: ')
    modules = module_names.strip().split(' ')

if len(modules[0]) < 1:                                             # use defaults if nothing provided
    modules = ['os', 'sys', 'string', 'subprocess', 'Customers', 'parser', 'foo']

whichmod(modules)
