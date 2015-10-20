import string
records = [
    ('cow', 'moon'),
    ('dolphin', 'highwire'),
    ('stuntman', 'bus')
]

tmpl = string.Template('The ${animal} jumped over the ${item}.')

for record in records:
    print(tmpl.substitute(animal=record[0], item=record[1]))