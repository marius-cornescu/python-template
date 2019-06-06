#!/usr/bin/env python
import os
from RtzanLibrary.core.common.version import VERSION

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
__version__ = VERSION
##########################################################################################################
DATE_TIME_FORMAT = '%Y.%m.%d %H:%M:%S%f'
PRINT_DATE_TIME_FORMAT = '%Y.%m.%d %H:%M:%S'
##########################################################################################################
def reloadConfigurations():
    from RtzanLibrary.core.common.configuration import APP_CONFIG, CONTROLLERS
    # application wide configuration data
    APP_CONFIG.reload()
    # controllers configuration data
    CONTROLLERS.reload()
    #
    CONTROLLERS_REPORT = ''
    if APP_CONFIG and CONTROLLERS:
        """
        """
        for ctrl_name, ctrl_app_cfg in APP_CONFIG['controllers'].items():
            try:
                enabled = ctrl_app_cfg.get('enable', '').lower() in ['true', 'yes']
                if enabled:
                    CONTROLLERS[ctrl_name] = updateControllerConfiguration(ctrl_app_cfg, CONTROLLERS.get(ctrl_name))
                    CONTROLLERS_REPORT = '%s%20s ... ON\n' % (CONTROLLERS_REPORT, ctrl_name.upper())
                else:
                    CONTROLLERS_REPORT = '%s%20s ... OFF\n' % (CONTROLLERS_REPORT, ctrl_name.upper())
            except Exception, e:
                CONTROLLERS_REPORT = '%s%20s ... ERROR( %s )\n' % (CONTROLLERS_REPORT, ctrl_name.upper(), e.message)
##########################################################################################################
def updateControllerConfiguration(ctrl_app_cfg, ctrl_config):
    """
    """
    if ctrl_config:
        if ctrl_app_cfg.__contains__('home'):
            if not os.path.isdir(ctrl_app_cfg['home']):
                raise Exception('Specified home path not accessible')
            #
            ctrl_config['binary'] = os.path.join(ctrl_app_cfg['home'], ctrl_config.get('binary', ''))
            ctrl_config['stop_binary'] = os.path.join(ctrl_app_cfg['home'], ctrl_config.get('stop_binary', ''))
            # for those with an external result converter
            if ctrl_config.__contains__('converter'):
                ctrl_config['converter']['binary'] = os.path.join(ctrl_app_cfg['home'], ctrl_config['converter'].get('binary', ''))
        #
        ctrl_config['app'] = ctrl_app_cfg
        #
    else:
        pass
    #
    return ctrl_config
##########################################################################################################
def getConfigOrDefault(config, default_config, parameter, default_value=None):
    """ Get the configuration from the main config object, or from the default config if missing or empty
    """
    value = config.get(parameter)
    if (value is None or value == '') and default_config is not None:
        value = default_config.get(parameter, default_value)
    return value
##########################################################################################################
