#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 18:46
import unittest
import logging

from onion_decorator.deprecated import deprecated

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@deprecated
def add(x, y):
    return x + y


class TestDeprecated(unittest.TestCase):
    def test_deprecated(self):
        self.assertEqual(add(1, 2), 1 + 2)
        self.assertEqual(add(2, 40), 2 + 40)
