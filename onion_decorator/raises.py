#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:52
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
NONE, MEDIUM, STRONG = 0, 1, 2


def raises(exceptions, debug=MEDIUM):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
                return ret
            except Exception as e:
                if not isinstance(e, exceptions):
                    if debug == NONE:
                        raise
                    elif debug == MEDIUM:
                        msg = "%s raised a unexpected exception: %s" % (f.__name__, repr(e))
                        logger.warning(msg)
                        raise
                    else:
                        msg = "%s raised a unexpected exception: %s" % (f.__name__, repr(e))
                        raise TypeError(msg)
                else:
                    raise

        return inner

    return outer


@raises(ValueError, debug=STRONG)
def foo():
    raise IndexError()

foo()
