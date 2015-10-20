class Contact:
    def __init__(self, name='', address='', phones=None, email='',
                 company='', position=''):
        self._name = name
        self._address = address
        self._phones = phones
        self._email = email
        self._company = company
        self._position = position

    def display_columned(self, nw=20, aw=25, ew=20, cw=25, psw=30):
        return '{0:<{nw}} {1:<{aw}} {2}\n{3:<{ew}} {4:<{cw}} {5:<{psw}}'.format(self.name, self._address, self._phones, self._email, self._company, self._position, nw=nw, aw=aw, ew=ew, cw=cw, psw=psw)

    def __str__(self):
        return '{0} {1}'.format(self._name, self._address)

    __repr__ = __str__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email:
            self._email = ''
        else:
            self._email = email