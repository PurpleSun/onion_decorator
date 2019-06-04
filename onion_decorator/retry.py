#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 22:42
import logging
from functools import wraps
import time


def retry(retries=5, catchable_exception=(Exception,), interval=None, logger=None):
    """
    :param retries: times want to retry
    :param catchable_exception: catchable exception types, must be tuple type
    :param interval: sleep time between two execution, in second unit
    :param logger: custom logger, default to None
    :return:
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            for i in xrange(retries):
                try:
                    logger.info("retry %s/%s" % (i + 1, retries))
                    return f(*args, **kwargs)
                except Exception as e:
                    if (i + 1) == retries:
                        logger.warning("still failed after %s retries, will re-raise exception", retries)
                        raise

                    if isinstance(e, catchable_exception):
                        logger.warning("got catchable exception", exc_info=True)
                        if interval is not None:
                            time.sleep(interval)
                        continue
                    else:
                        logger.error("got un-catchable exception, will re-raise exception", exc_info=True)
                        raise

        return inner

    return wrapper
