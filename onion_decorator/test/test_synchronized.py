#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 10:14
import logging
import threading
import unittest
from threading import Thread, RLock

from onion_decorator.synchronized import synchronized

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

number = 0


class TestSynchronized(unittest.TestCase):
    def test_synchronized_method(self):
        class Calc(object):
            def __init__(self):
                self.number = 0

            @synchronized()
            def increase(self):
                print "%s: increase" % threading.current_thread().name
                self.number += 1

            @synchronized()
            def decrease(self):
                print "%s: decrease" % threading.current_thread().name
                self.number -= 1

        class MyThread(Thread):
            def __init__(self, calc, name=None):
                super(MyThread, self).__init__(name=name)
                self.calc = calc

            def run(self):
                cnt = 100
                while cnt >= 0:
                    cnt -= 1
                    self.calc.increase()
                    self.calc.decrease()

        c = Calc()
        threads = []
        for i in xrange(100):
            my_thread = MyThread(c, name="thread-%s" % i)
            threads.append(my_thread)
            my_thread.start()

        for my_thread in threads:
            my_thread.join()

        self.assertEqual(c.number, 0)

    def test_synchronized_function(self):
        lock = RLock()

        @synchronized(lock)
        def increase():
            global number
            print "%s: ++" % threading.current_thread().name
            number += 1

        @synchronized(lock)
        def decrease():
            global number
            print "%s: --" % threading.current_thread().name
            number -= 1

        class MyThread(Thread):
            def __init__(self, name=None):
                super(MyThread, self).__init__(name=name)

            def run(self):
                cnt = 100
                while cnt >= 0:
                    cnt -= 1
                    increase()
                    decrease()

        threads = []
        for i in xrange(100):
            my_thread = MyThread(name="thread-%s" % i)
            threads.append(my_thread)
            my_thread.start()

        for my_thread in threads:
            my_thread.join()

        self.assertEqual(number, 0)
