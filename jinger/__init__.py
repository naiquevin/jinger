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

