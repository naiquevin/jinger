import os
from optparse import OptionParser
import sys
import logging


# For being able to test commands without intallation
# TODO - Replace with an elegant method
if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


from jinger import site
from jinger.config import get_config
from jinger.generator import generate_html, generate_webassets
from jinger.server import startserver
from jinger.exceptions import NotJingerPoweredError


logger = logging.getLogger('jinger')


def startsite():
    parser = OptionParser()
    parser.add_option("-s", "--sourcedir", dest="sourcedir",
                      help="Name of the dir for source template files (defaults to 'templates')")
    parser.add_option("-t", "--targetdir", dest="targetdir",
                      help="Name of the dir for generated html files (defaults to 'public')")

    (options, args) = parser.parse_args()

    try:
        sitename = args[1]
        opts = dict([(k, v) for k, v in options.__dict__.iteritems() if v is not None])
        site.create_empty_site(sitename, os.getcwd(), **opts)
    except IndexError:
        logger.error("Error: Please specify a name for the jinger powered site.")
        help()


def generate():
    try:
        conf = get_config(os.getcwd())

        # delete contents of the target dir
        
        

        generate_html(os.getcwd(), conf)
        generate_webassets(os.getcwd(), conf)
    except NotJingerPoweredError:
        logger.error("Error: Could not generate html as this doesn't seem to be a Jinger powered static site")
        help()


def runserver():
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="port",
                      help="Port to use for localhost (127.0.0.1)")

    (options, args) = parser.parse_args()

    port = options.port if options.port is not None else 9000

    try:
        startserver(port)
    except NotJingerPoweredError:
        logger.error("Error: Could not start server as this doesn't seem to be a Jinger powered static site")
        help()


def help():
    help_msg = """
    Available Commands:

    jinja startsite      Create directory structure for new static website
    jinja generate       Generate markup from template files
    jinja runserver      Start a development server

    Options:

      startsite:
        --sourcedir (-s) Name of the jinja2 templates directory (default: templates)
        --targetdir (-t) Name of the compiled markup files (default: public)

      runserver:
        --port (-p)      Port to use for the development server (default: 9000)

    Note: The commands `generate` and `runserver` need to be run from a directory
    which is a jinger powered website.

    """
    logger.info(help_msg)


def main():
    try:
        cmd = sys.argv[1]
    except IndexError:
        cmd = 'help'

    if cmd == 'startsite':
        startsite()
    elif cmd == 'generate':
        generate()
    elif cmd == 'runserver':
        runserver()
    elif cmd in ['help']:
        help()
    else:
        help()


# For being able to test commands without intallation
# TODO - Replace with an elegant method
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'startsite':
        startsite()
    elif cmd == 'generate':
        generate()
    elif cmd == 'runserver':
        runserver()
