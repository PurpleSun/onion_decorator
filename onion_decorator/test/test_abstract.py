#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:49
from onion_decorator.abstract import abstract


class Foo(object):
    @abstract
    def bar(self):
        pass


foo = Foo()
foo.bar()
