#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from piece import Bishop
from board import Board
from position import Position


class TestBishop(TestCase):
    def setUp(self):
        self.bishop = Bishop(Position(2, 2), Board(5, 5))

    def test_attacked_positions(self):
        self.assertSetEqual(self.bishop.attacked_positions,
                            {
                                Position(0, 0),
                                Position(1, 1),
                                Position(3, 3),
                                Position(4, 4),
                                Position(0, 4),
                                Position(1, 3),
                                Position(3, 1),
                                Position(4, 0)
                            })

    def test__str__(self):
        self.assertEqual(str(self.bishop), "B")
