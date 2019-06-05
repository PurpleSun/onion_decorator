#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:24
import logging
from functools import wraps

from onion_decorator.constant import NONE, MEDIUM, STRONG

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def accepts(*types, **kw):
    """
    Check the parameter types of the function

    @accepts(int, int, debug=MEDIUM)
    def add(x, y):
        return x + y

    print add(2, 40)

    :param types: expected parameter type
    :param kw:
        debug:
        1. NONE: check off, for production code
        2. MEDIUM: check on, only record warning log if checking failed
        3. STRONG: check on, raise TypeError if checking failed
    """
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
                assert len(types) == len(args)
                for i, arg in enumerate(args):
                    t = types[i]
                    if not isinstance(arg, t):
                        msg = "invalid arg for function '%s', arg %s is not type of %s" % (f.__name__, arg, t)
                        if debug == MEDIUM:
                            logger.warning(msg)
                            return f(*args)
                        elif debug == STRONG:
                            raise TypeError(msg)
                return f(*args)

            return inner

    return outer


