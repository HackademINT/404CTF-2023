from jinja2 import Template
import sys

with open('main.pony.j2', 'r') as f:
    template = Template(f.read())

with open('main.pony', 'w') as f:
    f.write(template.render(prgm = sys.argv[1]))