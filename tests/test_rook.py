#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from piece import Rook
from position import Position
from board import Board


class TestRook(TestCase):
    def setUp(self):
        self.rook = Rook(Position(2, 2), Board(5, 5))

    def test_attacked_positions(self):
        self.assertSetEqual(self.rook.attacked_positions,
                            {
                                Position(0, 2),
                                Position(1, 2),
                                Position(3, 2),
                                Position(4, 2),
                                Position(2, 0),
                                Position(2, 1),
                                Position(2, 3),
                                Position(2, 4)
                            })

    def test__str__(self):
        self.assertEqual(str(self.rook), "R")
