#!/usr/bin/env python
# -*- coding: utf-8 -*-

from singleton import Singleton
from piece import Piece
from position import Position


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
        self.squares = [[Empty] * cols for i in range(rows)]

    def __str__(self):
        line = '+' + '-+' * self.n_cols + '\n'
        return line + line.join('|' + '|'.join(str(square) for square in row) + '|\n' for row in self.squares) + line

    def __repr__(self):
        return ''.join(str(square) for rows in self.squares for square in rows)  # Yes, it's awkward

    def __hash__(self):
        return hash(repr(self))

    def __getitem__(self, key):
        return self.squares[key]

    def __eq__(self, other):
        return repr(self) == repr(other)

    @property
    def n_rows(self):
        return len(self.squares)

    @property
    def n_cols(self):
        return len(self.squares[0])

    def __contains__(self, pos):
        """
        :param pos: piece.piece.Position instance (row, col)
        :return: Whether this position falls within the board range or not
        """
        return 0 <= pos.col < self.n_cols and 0 <= pos.row < self.n_rows

    def place(self, piece_type, position):
        """ Places a *new* piece instance at the given position.
        Requires the location to be free.
        Piece type must be a subclass of Piece.

        :param piece: a piece type (Rook, Queen, Bishop, King, Knight). Must be subclass of Piece.
        :param position: a Position instance
        """
        assert isinstance(position, Position)
        assert position in self, "%s of of Range. Board dimensions are %ix%i" % (position, self.n_rows, self.n_cols)
        assert self[position.row][position.col] is Empty, "There is already a piece (%s) at %s" % \
                                                          (piece_type.__name__, position)
        assert issubclass(piece_type, Piece), "Piece Type must be subclass of Piece"

        self[position.row][position.col] = piece_type(position, self)

    def place_at(self, piece_type, row, col):
        """ Like above, but using row, col parameters for commodity.
        Requires the location to be free.
        Piece type must be a subclass of Piece.

        :param piece: a piece type (Rook, Queen, Bishop, King, Knight). Must be subclass of Piece.
        :param row: Row coordinate
        :param col: Column coordinate
        """
        self.place(piece_type, Position(row, col))
