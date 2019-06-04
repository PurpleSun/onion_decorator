#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 22:30
import unittest
import logging

from onion_decorator.timeit import timeit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@timeit("factorial", logger=logger)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


class TestTimeit(unittest.TestCase):
    def test_timeit(self):
        ret = factorial(10)
        self.assertEqual(ret, 3628800)
