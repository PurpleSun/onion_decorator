#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:48
from functools import wraps


def abstract(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        msg = "can't invoke abstract method '%s'" % f.__name__
        raise NotImplementedError(msg)

    return wrapper
