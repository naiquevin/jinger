#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

searchpath = os.path.abspath('templates')
targetpath = os.path.abspath('public')

env = Environment(loader=FileSystemLoader(searchpath))

# skip files which are base files. These will be prefixed with 'base'
templates = env.list_templates(filter_func=lambda x: not x.startswith('base') and x.endswith('.html'))

for t in templates:
    filepath = os.path.join(targetpath, *tuple(t.split(os.path.sep)))
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filepath, 'w') as f:
        f.writelines(env.get_template(t).generate())

