import os

from jinger.test import JingerPlaygroundTest, DIR_PLAYGROUND
from jinger.server import get_content, webasset_path
from jinger.site import create_empty_site

class WebContentTest(JingerPlaygroundTest):

    def setUp(self):
        super(WebContentTest, self).setUp()
        create_empty_site('mysite', DIR_PLAYGROUND)
        self.site = os.path.abspath(os.path.join(DIR_PLAYGROUND, 'mysite'))

        with open(os.path.join(self.site, 'templates', 'index.html'), 'w') as f:
            f.write('<!DOCTYPE html>')

        with open(webasset_path(self.site, 'styles.css'), 'w') as f:
            f.write('html, body {}')

        with open(webasset_path(self.site, 'main.js'), 'w') as f:
            f.write('var MYSITE = {};')

        with open(webasset_path(self.site, 'logo.png'), 'w') as f:
            f.write('100011')


    def test_get_content(self):
        content = get_content('/index.html', rootpath=self.site)
        self.assertEqual(content, '<!DOCTYPE html>')
        content = get_content('/styles.css', rootpath=self.site)
        self.assertEqual(content, 'html, body {}')
        content = get_content('/main.js', rootpath=self.site)
        self.assertEqual(content, 'var MYSITE = {};')
        content = get_content('/logo.png', rootpath=self.site)
        self.assertEqual(content, '100011')

