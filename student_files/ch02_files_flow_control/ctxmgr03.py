class CtxMgr(object):
    def __enter__(self):
        print('enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('exiting')
        if typ:
            print('Exception raised: {0}'.format(value))
        return False


with CtxMgr() as obj:
    int(obj)                # generates an exception
    print(obj)