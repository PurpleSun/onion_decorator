#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/5/31 21:52
import time
from Queue import Queue
from threading import Thread, RLock


class asynchronous(object):
    """
    makes function asynchronous
    """
    def __init__(self, func):
        self.func = func
        self.order = 0
        self.queues = {}
        self.lock = RLock()

        def threaded(*args, **kwargs):
            order = kwargs.pop("__order__")
            try:
                ret = self.func(*args, **kwargs)
                self.queues[order].put((None, ret))
            except Exception as e:
                self.queues[order].put((e, None))

        self.threaded = threaded

    def __call__(self, *args, **kwargs):
        # backup for synchronize invoking
        return self.func(*args, **kwargs)

    def async(self, *args, **kwargs):
        with self.lock:
            order = self.order
            self.order += 1
        kwargs["__order__"] = order
        queue = Queue()
        self.queues[order] = queue
        thread = Thread(target=self.threaded, args=args, kwargs=kwargs)
        thread.start()
        return asynchronous.Result(queue, thread)

    class NotYetDoneException(Exception):
        def __init__(self, message):
            self.message = message

    class Result(object):
        def __init__(self, queue, thread):
            self.queue = queue
            self.thread = thread

        def is_done(self):
            is_alive = not self.thread.is_alive()
            return is_alive

        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException("the call has not yet completed its task")

            if not hasattr(self, "result"):
                self.result = self.queue.get(timeout=1)

            return self.result


class WaitGroup(object):
    def __init__(self, group, interval=1e-3):
        self.group = group
        self.interval = interval

    def get(self):
        while not all([g.is_done() for g in self.group]):
            time.sleep(self.interval)
        return [g.get_result() for g in self.group]
