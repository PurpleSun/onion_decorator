#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 01:01
from threading import RLock


def synchronized(lock=None):
    if lock is not None:
        # normal function mode
        def outer(f):
            def inner(*args, **kwargs):
                with lock:
                    return f(*args, **kwargs)

            return inner

        return outer
    else:
        # class method mode
        def outer(f):
            def inner(self, *args, **kwargs):
                if not hasattr(self, "_lock"):
                    self._lock = RLock()
                with self._lock:
                    return f(self, *args, **kwargs)

            return inner

        return outer
