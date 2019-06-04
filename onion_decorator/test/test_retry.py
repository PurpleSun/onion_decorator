#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/29 23:23
import unittest
import logging

from onion_decorator.retry import retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@retry(retries=5, catchable_exception=(ValueError,), logger=logger)
def raise_value_error():
    raise ValueError()


cnt = 1


@retry(retries=5, catchable_exception=(Exception,), interval=0.5, logger=logger)
def returns_true():
    global cnt
    if cnt <= 4:
        cnt += 1
        raise KeyError()
    return True


class TestRetry(unittest.TestCase):
    def test_value_error(self):
        try:
            raise_value_error()
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_catch_all(self):
        ret = returns_true()
        self.assertEqual(ret, True)
