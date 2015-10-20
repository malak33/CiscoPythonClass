class Contact(object):
    def __init__(self, name='', address='', phones=None):
        self.name = name
        self.address = address
        self.phones = phones

    def __str__(self):
        return '{name} {address} {phones}'.format(**self.__dict__)


class BusinessContact(Contact):
    def __init__(self, name='', address='', phones=None,
                 email='', company='', position=''):
        super(BusinessContact, self).__init__(name, address, phones)
        self.email = email
        self.company = company
        self.position = position


bc = BusinessContact('John Smith', '123 Main St.', {'work': '(970)322-9088', 'home': '(970)455-2390'})
print(bc)