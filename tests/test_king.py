#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from board import Board
from piece import King
from position import Position

class TestQueen(TestCase):
    def setUp(self):
        self.queen = King(Position(2, 2), Board(5, 5))

    def test_attacked_positions(self):
        self.assertSetEqual(self.queen.attacked_positions,
                            {
                                Position(row=1, col=2),
                                Position(row=3, col=2),
                                Position(row=1, col=3),
                                Position(row=3, col=3),
                                Position(row=3, col=1),
                                Position(row=2, col=1),
                                Position(row=2, col=3),
                                Position(row=1, col=1)
                            })

    def test__str__(self):
        self.assertEqual(str(self.queen), "K")
