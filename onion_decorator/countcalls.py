#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 23:52
import time
from threading import Lock


class countcalls(object):
    def __init__(self, f):
        self.__doc__ = f.__doc__
        self.f = f
        self.count = 0
        self.elapse = 0
        self.lock = Lock()

    def __call__(self, *args, **kwargs):
        elapse = time.time()
        ret = self.f(*args, **kwargs)
        elapse = time.time() - elapse
        with self.lock:
            self.count += 1
            self.elapse += elapse
        return ret

    def tell(self):
        avg = self.elapse / self.count
        qps = 1.0 / avg
        return self.count, self.elapse, avg, qps


@countcalls
def add(x, y):
    """abc"""
    return x + y


@countcalls
def minus(x, y):
    """efg"""
    return x - y


d = time.time()
for _ in xrange(int(1e6)):
    add(2, 40)
    add(2, 40)
    minus(2, 1)
d = time.time() - d
print d

print add.tell()
print minus.tell()
