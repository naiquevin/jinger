import os
import logging
import shutil
from jinja2 import Environment, FileSystemLoader


logger = logging.getLogger('jinger')


def generate_html(sitedir, conf):
    """
    Compile Jinja2 templates in `sourcedir` to html files saved in
    `targetdir` preserving the directory structure.
    """
    sourcedir, targetdir = conf['sourcedir'], conf['targetdir']
    def filter_templates(x):
        return not x.startswith('base') and x.endswith('.html')

    env = Environment(loader=FileSystemLoader(conf['sourcedir']))    
    templates = env.list_templates(filter_func=filter_templates)
    for t in templates:
        filepath = os.path.join(targetdir,
                                *tuple(t.split(os.path.sep)))
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filepath, 'w') as f:
            f.writelines(env.get_template(t).generate())
            logger.info("Generated %s" % filepath)


def generate_webassets(sitedir, conf):
    """
    Generate or rather copy the contents of the `webassets` 
    directory to the `public` directory
    """
    ignore = shutil.ignore_patterns(('*~', '.gitignore'))
    for p in os.listdir(os.path.join(sitedir, 'webassets')):
        srcpath = os.path.join(sitedir, 'webassets', p)
        trgtpath = os.path.join(sitedir, conf['targetdir'], p)
        shutil.copytree(srcpath, trgtpath, ignore=ignore)

