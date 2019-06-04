#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 23:43
import logging
import time
from threading import RLock
from functools import wraps

from pylru import lrucache


def memorize(size=256, logger=None, callback=None):
    """
    :param size: max number of cached object
    :param logger: custom logger
    :param callback: callback function, will be called while cache ejected
    :return: memorized function
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    if callback is None:
        def callback(key, value):
            logger.info("cache %s ejected: %s", key, value)

    cache = lrucache(size, callback=callback)
    lock = RLock()

    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            key = "%s-%s" % (str(args), str(kwargs))
            if key in cache:
                logger.info("hint cache %s", key)
                return cache[key]
            else:
                with lock:
                    if cache in cache:
                        logger.info("hint cache %s", key)
                        return cache[key]
                    ret = f(*args, **kwargs)
                    cache[key] = ret
                    logger.info("cache %s updated", key)
                    return ret

        return inner

    return outer
