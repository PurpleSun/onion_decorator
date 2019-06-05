#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:35
import logging
from functools import wraps

from onion_decorator.accepts import accepts
from onion_decorator.constant import NONE, MEDIUM, STRONG

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def returns(*types, **kw):
    if not kw:
        # default level
        debug = MEDIUM
    else:
        debug = kw["debug"]

    def outer(f):
        if debug == NONE:
            return f
        elif debug == MEDIUM:
            @wraps(f)
            def inner(*args):
                ret = f(*args)
                if len(types) == 1:
                    t = types[0]
                    if not isinstance(ret, t):
                        msg = "invalid return for function '%s', %s is not type of %s" % (f.__name__, repr(ret), t)
                        if debug == MEDIUM:
                            logger.warning(msg)
                        elif debug == STRONG:
                            raise TypeError(msg)
                else:
                    assert len(types) == len(ret)
                    for i, r in enumerate(ret):
                        t = types[i]
                        if not isinstance(r, t):
                            msg = "invalid return for function '%s', %s is not type of %s" % (f.__name__, repr(r), t)
                            if debug == MEDIUM:
                                logger.warning(msg)
                            elif debug == STRONG:
                                raise TypeError(msg)
                return ret

            return inner

    return outer


@accepts(int, int, debug=MEDIUM)
@returns(int, debug=MEDIUM)
def add(x, y):
    return x + y


print add(2, 40)
