#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 00:33
import unittest
import logging

from onion_decorator.suppress_exception import suppress_exception

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@suppress_exception
def raise_no_exception():
    raise IOError()


class TestSuppressExceptions(unittest.TestCase):
    def test_raise_exception(self):
        raise_no_exception()
        self.assertTrue(True)
