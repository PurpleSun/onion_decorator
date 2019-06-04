#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/30 23:38
import dis
import sys

if sys.version < '3':
    def itemint(x):
        return ord(x)
else:
    def itemint(x):
        return x

    long = int


def override(f):
    bases = _get_base_classes(sys._getframe(2), f.__globals__)
    f_name = f.__name__
    inherited_f = _find_inherited_f(bases, f_name)
    if inherited_f is None:
        raise AssertionError("found no super class method for '%s'" % f_name)
    else:
        if not f.__doc__:
            f.__doc__ = inherited_f.__doc__
        return f


def _find_inherited_f(bases, f_name):
    for base in bases:
        f = getattr(base, f_name, None)
        if callable(f) and getattr(f, "__finalized__", False) is False:
            return f

    return None


def _get_base_classes(frame, namespace):
    return [_get_base_class(class_name_components, namespace) for
            class_name_components in _get_base_class_names(frame)]


def _get_base_class(components, namespace):
    try:
        obj = namespace[components[0]]
    except KeyError:
        obj = namespace["__builtins__"][components[0]]
    for component in components[1:]:
        obj = getattr(obj, component)
    return obj


def _get_base_class_names(frame):
    """ Get baseclass names from the code object """
    co, lasti = frame.f_code, frame.f_lasti
    code = co.co_code

    extends = []
    for (op, oparg) in op_stream(code, lasti):
        if op in dis.hasconst:
            if type(co.co_consts[oparg]) == str:
                extends = []
        elif op in dis.hasname:
            if dis.opname[op] == 'LOAD_NAME':
                extends.append(('name', co.co_names[oparg]))
            elif dis.opname[op] == 'LOAD_ATTR':
                extends.append(('attr', co.co_names[oparg]))
            elif dis.opname[op] == 'LOAD_GLOBAL':
                extends.append(('name', co.co_names[oparg]))

    items = []
    previous_item = []
    for t, s in extends:
        if t == 'name':
            if previous_item:
                items.append(previous_item)
            previous_item = [s]
        else:
            previous_item += [s]
    if previous_item:
        items.append(previous_item)
    return items


def op_stream(code, max):
    """Generator function: convert Python bytecode into a sequence of
    opcode-argument pairs."""
    i = [0]

    def next():
        val = itemint(code[i[0]])
        i[0] += 1
        return val

    ext_arg = 0
    while i[0] <= max:
        op = next()
        if op > dis.HAVE_ARGUMENT:
            arg = next() + (next() << 8)
        else:
            assert ext_arg == 0
            arg = 0  # unused

        if op == dis.EXTENDED_ARG:
            ext_arg += arg
            ext_arg <<= 16
            continue
        else:
            yield (op, arg + ext_arg)
            ext_arg = 0
