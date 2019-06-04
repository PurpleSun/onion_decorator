#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 23:53
import unittest
import logging
import time

from onion_decorator.memorize import memorize


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@memorize(size=100)
def memorized_fib(n):
    if n <= 1:
        return 1
    else:
        return memorized_fib(n - 1) + memorized_fib(n - 2)


class TestMemorize(unittest.TestCase):
    def setUp(self):
        self.n = 35

    def test_memorize(self):
        elapse1 = time.time()
        fib(self.n)
        elapse1 = time.time() - elapse1

        elapse2 = time.time()
        memorized_fib(self.n)
        elapse2 = time.time() - elapse2
        print elapse1
        print elapse2
        self.assertTrue(elapse1 > elapse2)

