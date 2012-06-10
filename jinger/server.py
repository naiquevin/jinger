import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader
import mimetypes

from jinger.config import get_config


_env = None


def get_env(rootpath=os.getcwd()):
    """
    Function for getting the jinja2 template environment instance so
    that it's loaded only once.
    """
    global _env
    if _env is None:
        conf = get_config(rootpath)
        templatepath = os.path.join(rootpath, conf['sourcedir'])
        _env = Environment(loader=FileSystemLoader(templatepath))
    return _env


class Http404(Exception):
    pass


class JingerHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        rootpath = os.getcwd()
        self.path = '/index.html' if self.path == '/' else self.path
        ctype = mimetypes.guess_type(self.path)[0]
        try:
            self.send_response(200)
            self.send_header('Content-type', ctype)
            self.end_headers()
            self.wfile.write(get_content(self.path, rootpath, ctype))
        except Http404:
            self.send_error(404, 'Template not found for path: %s' % self.path)


def get_content(path, rootpath=os.getcwd(), ctype=None):
    ctype = mimetypes.guess_type(path)[0] if ctype is None else ctype
    if ctype == 'text/html':
        return compiled_template_content(path, rootpath)
    elif webasset_exists(rootpath, path):
        return webassets_content(path, rootpath)
    elif ctype == 'image/x-icon':
        return ''
    else:
        raise Http404


def compiled_template_content(path, rootpath):
    templatepath = path.strip('/')
    try:
        env = get_env(rootpath)
        return env.get_template(templatepath).render()
    except IOError:
        raise Http404


def webassets_content(path, rootpath):
    try:
        with open(webasset_path(rootpath, path)) as f:
            return f.read()
    except IOError:
        raise Http404


def webasset_path(rootpath, path):
    return os.path.join(rootpath, 'webassets', path.strip('/'))


def webasset_exists(rootpath, path):
    return os.path.exists(webasset_path(rootpath, path))


def startserver(port):
    try:
        server = HTTPServer(('', int(port)), JingerHTTPRequestHandler)
        print 'Development server started at 127.0.0.1 on port %s' % port
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down server'
        server.socket.close()


if __name__ == '__main__':
    startserver()

