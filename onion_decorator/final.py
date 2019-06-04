#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 18:30


def final(f):
    setattr(f, "__finalized__", True)
    return f

