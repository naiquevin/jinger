"""
All code dealing with the directory structure for a jinger site.
"""
import os
import logging

from jinger import config


logger = logging.getLogger('jinger')

def createdir(path, dirname):
    path = os.path.join(path, dirname)
    if os.path.exists(path):
        raise Exception("A directory by name %s already exists" % path)
    logger.info("Creating path %s.." % path)
    os.mkdir(path)
    return path


def create_empty_site(sitename, cwd, sourcedir='templates', targetdir='public'):
    """
    Will create a directory of with the specified `sitename` in the
    `cwd`.

    `sourcedir` is for jinja2 template files
    `targetdir` is where the compiled html files will be placed.

    Additionally, a json config file will be created with 
    settings for the `sourcedir` and the `targetdir` so that these
    may be changed later on too and a directory named `webassets` 
    will be added where css, js etc files can be placed
    """
    logger.info("Creating site %s.." % sitename)

    sitedir = createdir(cwd, sitename)

    createdir(sitedir, sourcedir)
    createdir(sitedir, targetdir)

    createdir(sitedir, 'webassets')

    config.create(sitedir, sourcedir, targetdir)

    logger.info("DONE")


