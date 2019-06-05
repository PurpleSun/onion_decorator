#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:48
from functools import wraps
import logging

logger = logging.getLogger(__name__)


def abstract(f):
    """
    make method abstract.

    class Foo(object):
        @abstract
        def bar(self):
            pass

    foo = Foo()
    foo.bar()    # NotImplementedError: can't invoke abstract method 'bar'
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        msg = "can't invoke abstract method '%s'" % f.__name__
        logger.error(msg)
        raise NotImplementedError(msg)

    return wrapper
