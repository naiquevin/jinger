import os
import shutil
import logging

# setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')

logger = logging.getLogger('jinger')

if not logger.handlers:
    console = logging.StreamHandler()
    logger.addHandler(console)

logger.setLevel(logging.INFO)
logger.propagate = 0


def emptydir(dirpath, skip=('.gitignore')):
    """
    Empty the directory at the path specified by `dirpath` 

    If `skip` is a non-empty tuple, don't delete the files and
    directories that are lited in the tuple
    """
    files = [os.path.join(dirpath, f) 
             for f in os.listdir(dirpath) 
             if f not in skip]
    for f in files:
        if os.path.isfile(f):
            os.unlink(f)
        else:
            shutil.rmtree(f)

