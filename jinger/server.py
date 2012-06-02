import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader

from jinger.config import get_config


class Http404(Exception):
    pass


class JingerHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            content_handler = web_content_factory(self.path)
            self.send_response(200)
            self.send_header('Content-type', content_handler.content_type)
            self.end_headers()
            self.wfile.write(content_handler.get_content())
        except Http404:
            self.send_error(404, 'Template not found for path: %s' % self.path)


def web_content_factory(path):
    """
    Function to sniff the content type of the file requested and
    return an instance of the correct WebContent subclass
    """
    if path.endswith(('/', '.html')):
        return HtmlContent(path)
    if path.endswith(('.png', '.jpeg', '.jpg', '.gif')):
        return ImageContent(path)
    if path.endswith('.css'):
        return CSSContent(path)
    if path.endswith('.js'):
        return JSContent(path)
    if path.endswith('favicon.ico'):
        return Favicon(path)


class WebContent(object):
    
    content_type = 'plain/text'

    def __init__(self, path, rootpath=os.getcwd()):
        self.path = path
        self.rootpath = rootpath


class JinjaTemplateContentMixin(object):

    env = None
    
    @classmethod
    def get_env(cls, rootpath):
        if cls.env is None:
            conf = get_config(rootpath)
            templatepath = os.path.join(rootpath, conf['sourcedir'])
            cls.env = Environment(loader=FileSystemLoader(templatepath))
        return cls.env

    def get_content(self):
        templatepath = self.path.strip('/')
        try:
            env = self.__class__.get_env(self.rootpath)
            return env.get_template(templatepath).render()
        except IOError:
            raise Http404


class HtmlContent(WebContent, JinjaTemplateContentMixin):

    content_type = 'text/html'

    def __init__(self, path, *args, **kwargs):
        super(HtmlContent, self).__init__(path, *args, **kwargs)
        self.path = '/index.html' if self.path == '/' else self.path


class WebAssetsContentMixin(object):
    
    def get_content(self):
        try:
            filepath = os.path.join(self.rootpath, self.path.strip('/'))
            with open(filepath) as f:
                return f.read()
        except IOError:
            raise Http404


class CSSContent(WebContent, WebAssetsContentMixin):    
    content_type = 'text/css'


class JSContent(WebContent, WebAssetsContentMixin):
    content_type = 'text/javascript'


class ImageContent(WebContent, WebAssetsContentMixin):
    
    @property
    def content_type(self):
        ext = os.path.splitext(self.path)[1]
        return 'image/%s' % ext.lower().strip('.')


class Favicon(WebContent, WebAssetsContentMixin):
    content_type = 'image/x-icon'

    def get_content(self):
        try:
            return WebAssetsContentMixin.get_content(self)
        except Http404:
            return ''


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

