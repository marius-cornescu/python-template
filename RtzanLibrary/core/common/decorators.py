#!/usr/bin/env python
import os

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
##########################################################################################################
def synchronized(lock):
    """
    Synchronization decorator.
    """
    def wrap(f):
        def new_function(*args, **kw):
            lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                lock.release()
        return new_function
    return wrap
#########################################
def threaded():
    """
    """
    def wrap(f):
        def new_function(*args, **kw):
            args[0].lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                args[0].lock.release()
        return new_function
    return wrap
#########################################
def singleton(cls):
    """Decorator to ensures a class follows the singleton pattern.

    Example:
      @singleton
      class MyClass:
          ...
    """
    instances = {}

    def getInstance(*args, **kw):
        if cls not in instances:
            try:
                instances[cls] = cls(*args, **kw)
            except TypeError:
                return None
        return instances[cls]

    return getInstance
#########################################
def exit_in_single_mode(config):
    """
    """
    def wrap(f):
        def new_function(*args, **kw):
            try:
                return f(*args, **kw)
            finally:
                if config.get('singlemode', '').lower() in ['true', 'yes']:
                    os._exit(0)
        return new_function
    return wrap
##########################################################################################################

