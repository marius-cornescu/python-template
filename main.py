#!/usr/bin/env python
import os
import sys
import uuid
import socket
from optparse import OptionParser

from RtzanLibrary.core.common.version import VERSION

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
##########################################################################################################
def validateParameters(opts):
    #
	sys.exit(1)
    #
#########################################
def start_app(opts):
    host = opts.address
    port = opts.port
    test_type = opts.test_type
    test_file = opts.test_file
    analyser = opts.analyser
    single = opts.single
    debug = options.debug
    #
    me = SingleInstance()
    #
    configuration.APP_ID = uuid.uuid1()
    configuration.APP_HOST = host
    configuration.APP_PORT = port
    #
#########################################
class SingleInstance:
    def __init__(self):
        import tempfile
        self.lockfile = os.path.normpath(tempfile.gettempdir() + '/rtzan_app.lock')
        if sys.platform == 'win32':
            try:
                # file already exists, we try to remove (in case previous execution was interrupted)
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(self.lockfile, os.O_CREAT|os.O_EXCL|os.O_RDWR)
            except OSError, e:
                if e.errno == 13:
                    print "Another instance is already running, quitting."
                    sys.exit(-1)
                print e.errno
                raise
        else: # non Windows
            import fcntl
            self.fp = open(self.lockfile, 'w')
            try:
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                print "Another instance is already running, quitting."
                sys.exit(-1)

    def __del__(self):
        if sys.platform == 'win32':
            if hasattr(self, 'fd'):
                os.close(self.fd)
                os.unlink(self.lockfile)

##########################################################################################################

#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = OptionParser(
        usage="usage: %prog",
        version="%prog " + VERSION
    )
    #
    parser.add_option(
        "-d", "--debug",
        action="store_true",
        dest="debug",
        help="debug mode"
    )
    #
    (options, args) = parser.parse_args()

    print '=============================================================================='

    from RtzanLibrary.core.common import log, configuration

    validateParameters(options)

    log.LOGGER.info('=============================================================================================')
    log.LOGGER.info('STARTING RTZAN APPLICATION v%s' % VERSION)
    log.LOGGER.info('=============================================================================================')
    log.LOGGER.info('Parameters: %s' % str(options))
    log.LOGGER.info('=============================================================================================')
    log.LOGGER.info('\n%s' % configuration.CONTROLLERS_REPORT)
    log.LOGGER.info('=============================================================================================')
    log.LOGGER.debug('Configuration: %s' % str(configuration.CONTROLLERS))
    log.LOGGER.debug('=============================================================================================')

    try:
        # Start the app
        start_app(options)
    except BaseException as e:
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        log.LOGGER.error(''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        sys.exit(1)

