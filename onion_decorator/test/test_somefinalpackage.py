#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 00:35
from onion_decorator.final import final


class SomeClass(object):

    def somewhat_fun_method(self):
        """LULZ"""
        return 'LOL'

    @final
    def somewhat_finalized_method(self):
        return "some_final"