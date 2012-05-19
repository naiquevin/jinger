import os
from optparse import OptionParser

from jinger import site
from jinger.config import get_config
from jinger.generator import generate_html

conf = get_config(os.getcwd())

def startsite():
    parser = OptionParser()
    parser.add_option("-s", "--sourcedir", dest="sourcedir", 
                      help="Name of the dir for source template files (defaults to 'templates')")
    parser.add_option("-t", "--targetdir", dest="targetdir",
                      help="Name of the dir for generated html files (defaults to 'public')")

    (options, args) = parser.parse_args()

    site.create_empty_site(args[0], os.getcwd(), **options)


def generate():
    generate_html(conf['sourcedir'], conf['targetdir'])

