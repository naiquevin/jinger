import os
from optparse import OptionParser

# For being able to test commands without intallation
# TODO - Replace with an elegant method
if __name__ == '__main__':
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


from jinger import site
from jinger.config import get_config
from jinger.generator import generate_html
from jinger.server import startserver


def startsite():
    parser = OptionParser()
    parser.add_option("-s", "--sourcedir", dest="sourcedir", 
                      help="Name of the dir for source template files (defaults to 'templates')")
    parser.add_option("-t", "--targetdir", dest="targetdir",
                      help="Name of the dir for generated html files (defaults to 'public')")

    (options, args) = parser.parse_args()
    
    sitename = args[1]
    opts = dict([(k, v) for k, v in options.__dict__.iteritems() if v is not None])

    site.create_empty_site(sitename, os.getcwd(), **opts)


def generate():
    conf = get_config(os.getcwd())
    generate_html(os.getcwd(), conf['sourcedir'], conf['targetdir'])


def runserver():
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="port", 
                      help="Port to use for localhost (127.0.0.1)")
    
    (options, args) = parser.parse_args()

    port = options.port if options.port is not None else 9000
    
    startserver(port)
    

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
