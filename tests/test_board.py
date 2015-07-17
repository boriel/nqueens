#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from board import Board
from position import Position
from piece import Rook, Queen, Knight


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board(5, 7)

    def test_n_rows(self):
        self.assertEqual(self.board.n_rows, 5)

    def test_n_cols(self):
        self.assertEqual(self.board.n_cols, 7)

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

    def test__contains__(self):
        M, N = 5, 7
        board = Board(M, N)
        self.assertIn(Position(M - 1, N - 1), board)
        self.assertNotIn(Position(-1, -1), board)
        self.assertNotIn(Position(M, N), board)

    def test_place(self):
        self.board.place(Rook, Position(3, 4))
        self.assertIsInstance(self.board[3][4], Rook)

    def test_place_at(self):
        self.board.place_at(Rook, 3, 4)
        self.assertIsInstance(self.board[3][4], Rook)

    def test_place_out_of_range(self):
        self.assertRaises(AssertionError, self.board.place, Rook, Position(7, 4))

    def test_place_is_empty(self):
        self.board.place_at(Rook, 3, 2)
        self.assertRaises(AssertionError, self.board.place, list, Position(3, 2))

    def test_place_is_subclass(self):
        self.assertRaises(AssertionError, self.board.place, list, Position(3, 2))

    def test_pieces(self):
        self.board.place_at(Rook, 3, 2)
        self.board.place_at(Queen, 1, 1)
        self.board.place_at(Knight, 2, 4)
        self.assertListEqual([str(x) for x in self.board.pieces], ['R', 'Q', 'N'])

    def test_copy(self):
        self.board.place_at(Rook, 3, 2)
        self.board.place_at(Queen, 1, 1)
        self.board.place_at(Knight, 2, 4)
        tmp = self.board.copy()
        self.assertEqual(self.board, tmp)
        self.assertIsNot(self.board, tmp)

    def test_attacked(self):
        self.board.place_at(Rook, 3, 2)
        self.board.place_at(Queen, 1, 1)
        self.board.place_at(Knight, 2, 4)
        self.assertSetEqual(self.board.attacked, set.union(*[x.attacked_positions for x in self.board.pieces]))
