#!/usr/bin/env python

import unittest
import glob
import sys


def create_test_suite(mod):
    if mod is None:
        test_file_strings = glob.glob('jinger/test/test_*.py')
        module_strings = [str[0:len(str)-3].replace('/', '.') for str in test_file_strings]
    else:
        module_strings = ['jinger.test.test_%s' % (mod)]
    suites = [unittest.defaultTestLoader.loadTestsFromName(s) for s in module_strings]
    testSuite = unittest.TestSuite(suites)
    return testSuite


if __name__ == '__main__':
    try:
        mod = sys.argv[1]
    except IndexError as e:
        mod = None
    testSuite = create_test_suite(mod);
    text_runner = unittest.TextTestRunner().run(testSuite)

