class Contact:
    def __init__(self, name='', address='', phones=None, email='',
                 company='', position=''):
        self.name = name
        self.address = address
        self.phones = phones
        self.email = email
        self.company = company
        self.position = position

    def display_columned(self, nw=20, aw=25, ew=20, cw=25, psw=30):
        return '{0:<{nw}} {1:<{aw}} {2}\n{3:<{ew}} {4:<{cw}} {5:<{psw}}'.format(self.name, self.address, self.phones, self.email, self.company, self.position, nw=nw, aw=aw, ew=ew, cw=cw, psw=psw)

    def __str__(self):
        return '{0}'.format(self.name)

    __repr__ = __str__