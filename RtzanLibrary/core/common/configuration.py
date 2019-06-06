#!/usr/bin/env python
import unittest
import configobj
import os

import RtzanLibrary

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
##########################################################################################################
UNIT_TEST = False
INTEGRATION_TEST = False
SYSTEM_TEST = False
SMOKE_TEST = False
##########################################################################################################
__LIB_HOME_PATH__ = os.path.join(os.path.dirname(RtzanLibrary.__file__), '..')
##########################################################################################################
# application wide configuration file
APP_CONFIG_FILE = "config/application_config.ini"
if os.path.isdir(__LIB_HOME_PATH__):
    APP_CONFIG_FILE = os.path.join(__LIB_HOME_PATH__, APP_CONFIG_FILE)
# application wide configuration data
APP_CONFIG = configobj.ConfigObj(APP_CONFIG_FILE)
#
LOGGING_CONFIG_FILE = "config/logging_config.yaml"
if os.path.isdir(__LIB_HOME_PATH__):
    LOGGING_CONFIG_FILE = os.path.join(__LIB_HOME_PATH__, LOGGING_CONFIG_FILE)
#
##########################################################################################################
APP_ID = ''
APP_NAME = APP_CONFIG['global'].get('app_name', '')
APP_HOST = '0.0.0.0'
APP_PORT = 9000
##########################################################################################################
USE_FILE_COMPRESSION = True
##########################################################################################################

#***************************************************************************************
class Test(unittest.TestCase):
    def test_global_config(self):
        try:
            required_sections = ['logging', 'global']
            #
            for section in required_sections:
                self.assertTrue(APP_CONFIG[section])
            pass
        except Exception as e:
            self.fail(e)

#***************************************************************************************

if __name__ == '__main__':
    unittest.main()
