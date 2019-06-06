#!/usr/bin/env python
import unittest

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
#########################################################################################################
from RtzanLibrary.core.common import configuration
configuration.UNIT_TEST = False
#########################################
from RtzanLibrary.core.common import log
from RtzanLibrary.core.common import util

print(configuration.CONTROLLERS_REPORT)

test_loader = unittest.TestLoader()
one_test = unittest.TestSuite()
one_test.addTests(test_loader.loadTestsFromModule(util))

unittest.TextTestRunner(verbosity=2).run(one_test)
