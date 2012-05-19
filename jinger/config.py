import os
import json
import logging


logger = logging.getLogger('jinger')

CONFIG_FILENAME = 'config.json'


def create(path, sourcedir, targetdir):
    with open(path, 'w') as c:
        json.dump({sourcedir: sourcedir, targetdir: targetdir}, c, indent=4)
        logger.info("Writing config file %s.." % path)


def get_config(sitepath):
    """
    Get config dict
    """
    fp = open(os.path.join(sitepath, 'config.json'))
    return json.load(fp)
    
