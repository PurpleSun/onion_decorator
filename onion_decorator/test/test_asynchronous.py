#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 22:51
import time

from onion_decorator.asynchronous import asynchronous, WaitGroup

if __name__ == "__main__":
    # sample usage

    @asynchronous
    def power(num):
        time.sleep(1)
        return num * num


    @asynchronous
    def add(x, y):
        time.sleep(1)
        # raise Exception(x + y)
        return x + y


    elapse = time.time()
    foo = power.async(2)
    bar = add.async(2, 3)
    baz = add.async(3, 3)
    wait_group = WaitGroup([foo, bar, baz])
    print wait_group.get()
    # print wait_group.get()
    print time.time() - elapse
