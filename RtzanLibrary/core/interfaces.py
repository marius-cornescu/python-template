#!/usr/bin/env python

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
##########################################################################################################
class KeyedMixin(object):
    """It's a very common case for an instance's comparisons with other instances to boil down to
    comparing a tuple for each with a few fields -- and then, hashing should be implemented on exactly the same basis.
    The __key__ special method addresses that need directly
    """
    def __eq__(self, other):
      return not self<other and not other<self
    def __ne__(self, other):
      return self<other or other<self
    def __gt__(self, other):
      return other<self
    def __ge__(self, other):
      return not self<other
    def __le__(self, other):
      return not other<self
    def __lt__(self, other):
        return self.__key__() < other.__key__()
    #
    def __hash__(self):
        return hash(self.__key__())
    #
    def __key__(self):
        raise NotImplementedError
    #################################################

##########################################################################################################