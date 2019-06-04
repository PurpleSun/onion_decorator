#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 18:41
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def deprecated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.warning("function '%s' is deprecated, please consider do not invoking it anymore!", f.__name__)
        return f(*args, **kwargs)

    return wrapper
