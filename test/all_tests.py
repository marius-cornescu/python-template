#!/usr/bin/env python
import unittest

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
###########################################################################################################
print '\n\n******************************************************************************************'
print 'CORE TESTS'
print '******************************************************************************************\n\n'
###########################################################################################################

from RtzanLibrary.core.common import configuration
configuration.UNIT_TEST = True
configuration.SMOKE_TEST = True
#########################################
from RtzanLibrary.core.common import log
from RtzanLibrary.core.common import util

core_modules = [
        configuration,
        log,
        util
]

test_loader = unittest.TestLoader()
core_tests = unittest.TestSuite()
for module in core_modules:
    core_tests.addTests(test_loader.loadTestsFromModule(module))

unittest.TextTestRunner(verbosity=2).run(core_tests)

###########################################################################################################
print '\n\n******************************************************************************************\n\n'
##########################################################################################################