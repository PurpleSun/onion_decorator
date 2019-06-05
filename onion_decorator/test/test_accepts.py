#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/5 11:08
import unittest
import logging

from onion_decorator.accepts import accepts
from onion_decorator.constant import NONE, MEDIUM, STRONG

logging.basicConfig(level=logging.INFO)


def add(x, y):
    return x + y


class TestAccepts(unittest.TestCase):
    @staticmethod
    def gen_f(debug):
        return accepts(int, str, debug=debug)(add)

    def test_debug_none(self):
        f_none = self.gen_f(NONE)
        ret = f_none(1, 2)
        self.assertEqual(ret, 3)

    def test_debug_medium(self):
        f_medium = self.gen_f(MEDIUM)
        ret = f_medium(1, 2)
        self.assertEqual(ret, 3)

    def test_debug_strong(self):
        f_strong = self.gen_f(STRONG)
        try:
            ret = f_strong(1, 2)
            self.assertNotEqual(ret, 3)
        except Exception as e:
            self.assertTrue(isinstance(e, TypeError))
