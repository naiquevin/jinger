import os

from jinger.test import JingerPlaygroundTest, DIR_PLAYGROUND
from jinger import server
from jinger.site import create_empty_site

class WebContentTest(JingerPlaygroundTest):

    def setUp(self):
        super(WebContentTest, self).setUp()
        create_empty_site('mysite', DIR_PLAYGROUND)
        self.site = os.path.abspath(os.path.join(DIR_PLAYGROUND, 'mysite'))
    

    def test_web_content_factory(self):
        inst_map = {
            server.HtmlContent: ['/index.html', '/products/index.html'],
            server.CSSContent: ['/css/styles.css'],
            server.JSContent: ['/js/main.js'],
            server.ImageContent: ['/images/star.jpg'],
            server.Favicon: ['/favicon.ico'],
            }

        for C, paths in inst_map.iteritems():
            for p in paths:
                inst = server.web_content_factory(p)
                self.assertIsInstance(inst, C)


    def test_html_content(self):        
        with open(os.path.join(self.site, 'templates', 'index.html'), 'w') as f:
            f.write('<!DOCTYPE html>')
        content = server.HtmlContent('/index.html', rootpath=self.site)
        self.assertEqual(content.content_type, 'text/html')
        self.assertEqual(content.get_content(), '<!DOCTYPE html>')


    def test_css_content(self):
        with open(os.path.join(self.site, 'styles.css'), 'w') as f:
            f.write('html, body {}')
        content = server.CSSContent('/styles.css', rootpath=self.site)
        self.assertEqual(content.content_type, 'text/css')
        self.assertEqual(content.get_content(), 'html, body {}')


    def test_js_content(self):
        with open(os.path.join(self.site, 'main.js'), 'w') as f:
            f.write('var MYSITE = {};')
        content = server.JSContent('/main.js', rootpath=self.site)
        self.assertEqual(content.content_type, 'text/javascript')
        self.assertEqual(content.get_content(), 'var MYSITE = {};')


    def test_image_content(self):
        with open(os.path.join(self.site, 'logo.png'), 'w') as f:
            f.write('100011')
        content = server.ImageContent('/logo.png', rootpath=self.site)
        self.assertEqual(content.content_type, 'image/png')
        self.assertEqual(content.get_content(), '100011')

