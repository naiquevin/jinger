import logging

# setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)-8s%(message)s',
                    datefmt='%m-%d %H:%M')

console = logging.StreamHandler()

logging.getLogger('jinger').addHandler(console)
logging.getLogger('jinger').setLevel(logging.INFO)

