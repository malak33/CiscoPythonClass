class Contact:
    def __init__(self, name='', address='', phone='', email='',
                 company='', position=''):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.company = company
        self.position = position

    def __str__(self):
        return '{0}'.format(self.name)


c = Contact('John Smith', '123 Main St.', '(970)322-9088',
            'jsmith433@yahoo.com', 'Acme Inc.', 'Rubber Hole Engineer')

c.alt_email = 'jsmith433@gmail.com'
print(c.name, c.alt_email)              # John Smith jsmith433@gmail.com
print(c, type(c))                       # John Smith <class '__main__.Contact'>
