#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 20:56
from threading import RLock

__all__ = ["singleton"]


def singleton(clazz):
    """
    :param clazz: a class
    :return: a singleton class
    """
    mem = {}
    lock = RLock()

    def inner(*args, **kwargs):
        with lock:
            if mem.get(clazz) is None:
                mem[clazz] = clazz(*args, **kwargs)
        return mem.get(clazz)

    return inner
