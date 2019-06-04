#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 00:51
import logging
from functools import wraps
from threading import RLock

logger = logging.getLogger(__name__)


def once(f):
    mem = {
        "called": False,
        "ret": None
    }
    lock = RLock()

    @wraps(f)
    def wrapper(*args, **kwargs):
        if not mem["called"]:
            with lock:
                if not mem["called"]:
                    logger.info("first call")
                    ret = f(*args, **kwargs)
                    mem["called"] = True
                    mem["ret"] = ret
                    return ret
                else:
                    logger.info("already called")
                    return mem["ret"]
        else:
            logger.info("already called")
            return mem["ret"]

    return wrapper
