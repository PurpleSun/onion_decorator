#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 00:54
import unittest
import logging

from onion_decorator.once import once

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@once
def add(x, y):
    return x + y


class TestOnce(unittest.TestCase):
    def test_once(self):
        a = add(1, 2)
        b = add(1, 2)
        self.assertEqual(a, b)
