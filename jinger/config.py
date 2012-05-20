import os
import json
import logging


logger = logging.getLogger('jinger')

CONFIG_FILENAME = 'config.json'


def create(path, sourcedir, targetdir):
    confpath = os.path.join(path, CONFIG_FILENAME)
    with open(confpath, 'w') as c:
        json.dump({"sourcedir": sourcedir, "targetdir": targetdir}, c, indent=4)
        logger.info("Writing config file %s.." % path)
    return confpath


def get_config(sitepath):
    """
    Get config dict
    """
    fp = open(os.path.join(sitepath, CONFIG_FILENAME))
    return json.load(fp)
    
