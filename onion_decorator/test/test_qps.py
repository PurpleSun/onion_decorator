#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 12:31
import time
import unittest
import logging

from onion_decorator.qps import qps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def dummy():
    pass


class TestQps(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def gen_f(n):
        return qps(n)(dummy)

    def test_qps(self):
        for max_qps in xrange(0, 50000, 1000):
            if max_qps == 0:
                max_qps = 1
            seconds = 10
            count = 0
            f = self.gen_f(max_qps)
            start = time.time()
            while time.time() - start <= seconds:
                f()
                count += 1

            real_qps = count / seconds
            logger.info("%s,%s", max_qps, real_qps)
            self.assertTrue(real_qps <= max_qps)
