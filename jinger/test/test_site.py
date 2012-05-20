# import unittest
import os

from jinger.site import create_empty_site, createdir
from jinger.test import DIR_PLAYGROUND, JingerPlaygroundTest

class SiteTest(JingerPlaygroundTest):

    def test_create_dir(self):
        mysite = createdir(DIR_PLAYGROUND, 'mysite')
        self.assertTrue(os.path.exists(mysite))

        # check that if the dir already exists, it raises an Exception
        pass

    def test_create_empty_site(self):
        create_empty_site('mysite', DIR_PLAYGROUND)
        newsite = os.path.join(DIR_PLAYGROUND, 'mysite')
        os.path.exists(newsite)
        os.path.exists(os.path.join(newsite, 'templates'))
        os.path.exists(os.path.join(newsite, 'public'))
        os.path.exists(os.path.join(newsite, 'config.json'))
        
        create_empty_site('myothersite', DIR_PLAYGROUND, '_source', 'www')
        newsite = os.path.join(DIR_PLAYGROUND, 'myothersite')
        os.path.exists(newsite)
        os.path.exists(os.path.join(newsite, '_source'))
        os.path.exists(os.path.join(newsite, 'www'))
        os.path.exists(os.path.join(newsite, 'config.json'))


