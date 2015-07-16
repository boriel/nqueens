#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from position import Position
from position import Direction

class TestPosition(TestCase):
    def setUp(self):
        self.pos = Position(3, 3)

    def test_North(self):
        self.assertEqual(self.pos.North, Position(2, 3))

    def test_South(self):
        self.assertEqual(self.pos.South, Position(4, 3))

    def test_East(self):
        self.assertEqual(self.pos.East, Position(3, 2))

    def test_West(self):
        self.assertEqual(self.pos.West, Position(3, 4))

    def test_NorthEast(self):
        self.assertEqual(self.pos.NorthEast, Position(2, 2))

    def test_SouthEast(self):
        self.assertEqual(self.pos.SouthEast, Position(4, 2))

    def test_NorthWest(self):
        self.assertEqual(self.pos.NorthWest, Position(2, 4))

    def test_SouthWest(self):
        self.assertEqual(self.pos.SouthWest, Position(4, 4))

    def test_N(self):
        self.assertEqual(self.pos.N(), Position(2, 3))

    def test_S(self):
        self.assertEqual(self.pos.S(), Position(4, 3))

    def test_E(self):
        self.assertEqual(self.pos.E(), Position(3, 2))

    def test_W(self):
        self.assertEqual(self.pos.W(), Position(3, 4))

    def test_NE(self):
        self.assertEqual(self.pos.NE(), Position(2, 2))

    def test_NW(self):
        self.assertEqual(self.pos.NW(), Position(2, 4))

    def test_SE(self):
        self.assertEqual(self.pos.SE(), Position(4, 2))

    def test_SW(self):
        self.assertEqual(self.pos.SW(), Position(4, 4))

    def test_go(self):
        self.assertEqual(
            [self.pos.go(x) for x in Direction],
            [
                Position(2, 3),
                Position(4, 3),
                Position(3, 2),
                Position(3, 4),
                Position(2, 2),
                Position(2, 4),
                Position(4, 2),
                Position(4, 4)
            ]
        )
