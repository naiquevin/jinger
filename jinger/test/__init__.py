import os
import unittest
import logging

from jinger import emptydir

# disable logging while running tests
logging.disable(logging.CRITICAL)


DIR_PLAYGROUND = os.path.dirname(os.path.realpath(__file__)) + '/../../playground'


def empty_playground():
    """
    Delete all file contents of the playground dir
    """
    emptydir(DIR_PLAYGROUND)


def ensure_empty_playground():
    if len(os.listdir(DIR_PLAYGROUND)) != 0:
        empty_playground()


class JingerPlaygroundTest(unittest.TestCase):

    def setUp(self):
        # ensure the playground dir is empty initially
        ensure_empty_playground()

    def tearDown(self):
        # ensure the playground dir is empty initially
        empty_playground()

