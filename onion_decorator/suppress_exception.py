#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 00:29
from functools import wraps
import logging


def suppress_exception(f):
    """
    exceptions suppressing decorator
    :param f: decorated function
    :return: return whatever the decorated function returns while execution is successful, otherwise None
    """
    logger = logging.getLogger(__name__)

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception:
            logger.warning("got suppressed exception while calling %s(args=%s, kwargs=%s)",
                           f.__name__, repr(args), repr(kwargs), exc_info=True)
            return None

    return wrapper
