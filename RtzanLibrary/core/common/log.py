#!/usr/bin/env python
import os
from string import maketrans
import sys
import logging
import logging.config

from RtzanLibrary.core.common import configuration

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
#############
LOGGER = None
STDLOGGER = None
##########################################################################################################
def __null_log():
    logger = logging.getLogger("null")
    # create console handler and set level to debug
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    #
    stdlogger = logging.getLogger("null")
    # create console handler and set level to debug
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    stdlogger.addHandler(handler)

    return logger, stdlogger

##########################################################################################################
#### MAIN CODE
##########################################################################################################
if configuration.APP_CONFIG is not None \
        and 'logging' in configuration.APP_CONFIG \
        and configuration.APP_CONFIG['logging'].get('enable', '').lower() in ['true', 'yes']:
    #
    from RtzanLibrary.core.common import custom_handlers
    logging.custom_handlers = custom_handlers
    #
    try:
        log_dir = os.path.abspath(configuration.APP_CONFIG['logging'].get('log_dir', 'logs'))
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
    except:
        pass
    #
    try:
        with open(configuration.LOGGING_CONFIG_FILE, 'rt') as f:
            import yaml
            log_config = yaml.load(f.read())
            logging.config.dictConfig(log_config)
            #
            LOGGER = logging.getLogger(configuration.APP_CONFIG['logging']['application_logger_name'])
            STDLOGGER = logging.getLogger(configuration.APP_CONFIG['logging']['stdout_logger_name'])
    except:
        LOGGER, STDLOGGER = __null_log()
    #
else:
    LOGGER, STDLOGGER = __null_log()
##########################################################################################################

##########################################################################################################
class StdOutWrapper:
    """ Call wrapper for stdout
    """
    def write(self, s):
        s = s.translate(maketrans('', ''), '\n\r')
        if s:
            STDLOGGER.info(s)

class StdErrWrapper:
    """ Call wrapper for stderr
    """
    def write(self, s):
        s = s.translate(maketrans('', ''), '\n\r')
        if s:
            STDLOGGER.warn(s)

##########################################################################################################
def _intercept_stdout():
    sys.stdout = StdOutWrapper()

def _restore_stdout():
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    return output

#########################################
def _intercept_stderr():
    sys.stderr = StdErrWrapper()

def _restore_stderr():
    output = sys.stderr.getvalue()
    sys.stderr.close()
    sys.stderr = sys.__stderr__
    return output

##########################################################################################################
class NullHandler(logging.Handler):
    def emit(self, record):
        print str(record)

##########################################################################################################
