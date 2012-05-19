import os
import logging
from jinja2 import Environment, FileSystemLoader

from jinger.config import conf

logger = logging.getLogger('jinger')

def generate_html(sourcedir, targetdir):
    """
    Compile Jinja2 templates in `sourcedir` to html files saved in `targetdir`
    preserving the directory structure.
    """
    def filter_templates(x):
        return not x.startswith('base') and x.endswith('.html')

    env = Environment(loader=FileSystemLoader(conf['sourcedir']))    
    templates = env.list_templates(filter_func=filter_templates)
    for t in templates:
        filepath = os.path.join(targetdir, *tuple(t.split(os.path.sep)))
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filepath, 'w') as f:
            f.writelines(env.get_template(t).generate())
            logger.info("Generated %s" % filepath)
    
