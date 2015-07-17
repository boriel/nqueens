#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from piece import Knight
from board import Board
from position import Position


class TestKnight(TestCase):
    def setUp(self):
        self.rook = Knight(Position(2, 2), Board(5, 5))

    def test_attacked_positions(self):
        self.assertSetEqual(self.rook.attacked_positions,
                            {
                                Position(0, 1),
                                Position(0, 3),
                                Position(4, 1),
                                Position(4, 3),
                                Position(1, 0),
                                Position(3, 0),
                                Position(1, 4),
                                Position(3, 4)
                            })

    def test__str__(self):
        self.assertEqual(str(self.rook), "N")
