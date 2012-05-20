import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader

from jinger.config import get_config


env = None


class Http404(Exception):
    pass


class JingerHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            self.wfile.write(get_html(self.path))
        except Http404:
            self.send_error(404, 'Template not found for path: %s' % self.path)


def get_html(path):
    global env
    templatepath = os.path.abspath(os.path.join(*tuple([s for s in path.split() if s])))
    try:
        return env.get_template(templatepath).generate()
    except IOError:
        raise Http404


def startserver(port):
    global env
    conf = get_config(os.getcwd())
    env = Environment(loader=FileSystemLoader(conf['sourcedir']))
    try:
        server = HTTPServer(('', int(port)), JingerHTTPRequestHandler)
        print 'Development server started at 127.0.0.1 on port %s' % port
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down server'
        server.socket.close()


if __name__ == '__main__':
    startserver()

