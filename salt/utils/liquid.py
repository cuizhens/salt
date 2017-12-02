# -*- coding: utf-8 -*-
'''
Utilities for the Liquid subsystem
'''
from __future__ import absolute_import
import logging

# Import salt libs
import salt.loader

log = logging.getLogger(__name__)


def fetch(opts, utils=None, **kwargs):
    '''
    Fetch the configuration options using the liquid module.
    '''
    if utils is None:
        utils = {}
    driver = 'yaml'  # TODO: get the driver name from the opts
    fun = '{0}.get'.format(driver)
    loaded_lq = salt.loader.liquid(opts, fun, utils=utils)
    return loaded_lq[fun](**kwargs)
