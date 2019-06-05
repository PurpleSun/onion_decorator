#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/1 00:49
import unittest
import logging

from onion_decorator.abstract import abstract

logging.basicConfig(level=logging.INFO)


class Foo(object):
    @abstract
    def bar(self):
        pass


class TestAbstract(unittest.TestCase):
    def test_abstract(self):
        try:
            foo = Foo()
            foo.bar()
        except Exception as e:
            self.assertTrue(isinstance(e, NotImplementedError))
