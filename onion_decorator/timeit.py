#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 21:21
import logging
from functools import wraps
import time


def timeit(tag="TIMEIT", logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            elapse = time.time()
            ret = f(*args, **kwargs)
            elapse = time.time() - elapse
            logger.info("[#%s] cost %s seconds for execution: %s(args=%s, kwargs=%s) => %s",
                        tag, round(elapse, 6), f.func_name, repr(args), repr(kwargs), repr(ret))

            return ret

        return inner

    return outer
