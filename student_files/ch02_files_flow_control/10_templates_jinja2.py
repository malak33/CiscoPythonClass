from jinja2 import Template

records = [
    ('cow', 'moon'),
    ('dolphin', 'highwire'),
    ('stuntman', 'bus')
]

tmpl = Template('The {{animal}} jumped over the {{item}}.')

for record in records:
    print(tmpl.render(animal=record[0], item=record[1]))



# -------------------------------------------------------
#   using templates
#
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound
env = Environment(loader=FileSystemLoader('./templates'))

try:
    tmpl = env.get_template('example_tmpl.jinja')
    print(tmpl.render(records=records))
    # can write results to a file as well
except (TemplateNotFound, TemplateError) as e:
    print('Error: {0} {1}'.format(type(e), e))