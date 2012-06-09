import os

from jinger import config
from jinger.test import DIR_PLAYGROUND, JingerPlaygroundTest

class ConfigTest(JingerPlaygroundTest):

    def setUp(self):
        super(ConfigTest, self).setUp()
        self.mysite = os.path.join(DIR_PLAYGROUND, 'mysite')
        os.mkdir(self.mysite)        
    
    def test_config(self):
        config.create(self.mysite, 'templates', 'public')

        conf = config.get_config(self.mysite)
        
        self.assertEqual(conf['sourcedir'], 'templates')
        self.assertEqual(conf['targetdir'], 'public')
        self.assertEqual(conf['skip_templates'], ['base*.html', '_*.html'])
        
