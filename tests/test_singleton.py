#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from singleton import Singleton


class TestSingleton(TestCase):
    def test_uniqueness(self):

        @Singleton
        class SingletonExample:
            pass

        a = SingletonExample()
        b = SingletonExample()
        self.assertIs(a, b)

