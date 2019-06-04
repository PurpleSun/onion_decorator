#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 21:01
import unittest

from onion_decorator.singleton import singleton


@singleton
class Atom(object):
    pass


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        foo = Atom()
        bar = Atom()
        baz = Atom()
        self.assertTrue(id(foo), id(bar))
        self.assertTrue(id(foo), id(baz))
        self.assertTrue(id(bar), id(baz))
