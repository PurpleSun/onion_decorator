#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 19:54
import time
import unittest
import logging

from onion_decorator.timeout import TimeoutError, timeout

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@timeout(2)
def add(x, y):
    time.sleep(1)
    return x + y


@timeout(1)
def minus(x, y):
    time.sleep(2)
    return x + y


class TestTimeout(unittest.TestCase):
    def test_timeout(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_timeout_exception(self):
        try:
            minus(2, 1)
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(isinstance(e, TimeoutError))
