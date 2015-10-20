from ch04_oo.modules.contacts2 import Contact

contact_list = []
try:
    with open('../resources/contacts.dat') as f:
        for line in f:
            contact_data = line.split(',')
            name, address = contact_data[:2]
            contact_list.append(Contact(name, address))
except IOError as e:
    print('Error: {0}'.format(e))


c = Contact('John Smith', '123 Main St.', [{'work':'(970)322-9088', 'home':'(970)455-2390'}],
            'jsmith433@yahoo.com', 'Acme Inc.', 'Rubber Hole Engineer')

print(c.__dict__['name'])