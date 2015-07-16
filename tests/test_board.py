#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from board import Board


class TestBoard(TestCase):
    def test_n_rows(self):
        board = Board(5, 7)
        self.assertEqual(board.n_rows, 5)

    def test_n_cols(self):
        board = Board(5, 7)
        self.assertEqual(board.n_cols, 7)

    def test_repr(self):
        board = Board(0, 0)
        self.assertEqual(repr(board), '')

        board = Board(3, 3)
        self.assertEqual(repr(board), 9 * ' ')

    def test_str(self):
        board = Board(1, 1)
        self.assertEqual(str(board), '+-+\n| |\n+-+\n')

    def test_eq(self):
        a = Board(5, 5)
        b = Board(5, 5)
        c = Board(3, 5)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test__hash__(self):
        c = {Board(5, 5)}
        c.add(Board(5, 5))
        self.assertEqual(len(c), 1)
