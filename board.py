#!/usr/bin/env python
# -*- coding: utf-8 -*-

from singleton import Singleton

@Singleton
class EmptySquare:
    """ Simple class to define an empty square.
    """
    def __repr__(self):
        return " "


# This should be a singleton,
# to use the python idiom Board[col][row] is Empty
Empty = EmptySquare()


class Board:
    """ Defines a M x N (Rows x Cols) checkboard.
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.squares = [[Empty] * self.cols for i in range(self.rows)]

    def __str__(self):
        line = '+' + '-+' * self.cols + '\n'
        return line + line.join('|' + '|'.join(str(square) for square in row) + '|\n' for row in self.squares) + line

    def __repr__(self):
        return ''.join(str(square) for rows in self.squares for square in rows)  # Yes, it's awkward

    def __hash__(self):
        return hash(repr(self))

    def __getitem__(self, key):
        return self.squares[key]
