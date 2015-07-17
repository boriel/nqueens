#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton:
    """ Provides a simple singleton decorator.
    NOTE: First Letter capitalized to follow pycharm strict PEP-8 convention
    """

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance
