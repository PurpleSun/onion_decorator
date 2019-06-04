#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 00:34
import unittest

from onion_decorator.override import override
import test_somepackage


class SuperClass(object):

    def some_method(self):
        """Super Class Docs"""
        return 'super'


class SubClass(SuperClass):

    @override
    def some_method(self):
        return 'sub'


class Subber(SuperClass):

    @override
    def some_method(self):
        """Subber"""
        return 1


class Sub2(test_somepackage.SomeClass, SuperClass):
    @override
    def somewhat_fun_method(self):
        return 'foo'

    @override
    def some_method(self):
        pass


class SubclassOfInt(int):
    @override
    def __str__(self):
        return "subclass of int"


class overrideTests(unittest.TestCase):
    def test_override_passes_for_same_package_superclass(self):
        sub = SubClass()
        self.assertEqual(sub.some_method(), 'sub')
        self.assertEqual(sub.some_method.__doc__, 'Super Class Docs')

    def test_override_does_not_override_method_doc(self):
        sub = Subber()
        self.assertEqual(sub.some_method(), 1)
        self.assertEqual(sub.some_method.__doc__, 'Subber')

    def test_override_passes_for_superclass_in_another_package(self):
        sub2 = Sub2()
        self.assertEqual(sub2.somewhat_fun_method(), 'foo')
        self.assertEqual(sub2.somewhat_fun_method.__doc__, 'LULZ')

    def test_assertion_error_is_thrown_when_method_not_in_superclass(self):
        try:
            class ShouldFail(SuperClass):
                @override
                def somo_method(self):
                    pass

            raise RuntimeError('Should not go here')
        except AssertionError:
            pass

    def test_can_override_builtin(self):
        x = SubclassOfInt(10)
        self.assertEqual(str(x), 'subclass of int')
