import os
import json
import logging

from jinger.exceptions import NotJingerPoweredError


logger = logging.getLogger('jinger')

CONFIG_FILENAME = 'config.json'


def create(path, sourcedir, targetdir):
    confpath = os.path.join(path, CONFIG_FILENAME)
    with open(confpath, 'w') as c:
        conf = {"sourcedir": sourcedir, 
                "targetdir": targetdir,
                "skip_templates": ['base*.html', '_*.html']}
        json.dump(conf, c, indent=4)
        logger.info("Writing config file %s.." % path)
    return confpath


def get_config(sitepath):
    """
    Get config dict
    """
    try:
        fp = open(os.path.join(sitepath, CONFIG_FILENAME))
        return json.load(fp)
    except IOError:
        raise NotJingerPoweredError

