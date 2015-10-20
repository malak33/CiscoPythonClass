class CtxMgr(object):
    def __enter__(self):
        print('enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('exiting')


with CtxMgr() as obj:
    print(obj)