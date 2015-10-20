class CtxMgr(object):
    def __enter__(self):
        print('enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('exiting')
        if typ:
            print('Exception raised: {0}'.format(value))
        return False


try:
    with CtxMgr() as obj:
        int(obj)                        # exception
        print(obj)
except ValueError as e:
    print('Handled {0}'.format(e))

