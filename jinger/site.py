"""
All code dealing with the directory structure for a jinger site.
"""
import os
import logging

from jinger import config


logger = logging.getLogger('jinger')

def createdir(path):
    if os.path.exists(path):
        raise Exception("A directory by name %s already exists" % path)
    logger.info("Creating path %s.." % path)
    os.mkdir(path)


def create_empty_site(sitename, cwd, sourcedir='templates', targetdir='public'):
    """
    Will create a directory of with the specified `sitename` in the
    `cwd`.

    `sourcedir` is for jinja2 template files
    `targetdir` is where the compiled html files will be placed.

    Additionally, a json config file will also be created with 
    settings for the `sourcedir` and the `targetdir` so that these
    may be changed later on too.
    """
    logger.info("Creating site %s.." % sitename)

    paths = map(lambda a: os.path.abspath(os.path.join(*a)),
                [(cwd, sitename),
                 (cwd, sitename, config.CONFIG_FILENAME),
                 (cwd, sitename, sourcedir),
                 (cwd, sitename, targetdir)])

    sitedir, configfile, source, target = paths

    createdir(sitedir)
    createdir(source)
    createdir(target)

    config.create(configfile, sourcedir, targetdir)

    logger.info("DONE")


