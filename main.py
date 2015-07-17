#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board import Board, Empty
from piece import King, Queen, Rook, Bishop, Knight
from position import Position

M, N = 3, 3
pieces = [King, King, Rook]

board = Board(M, N)
SOLUTIONS = {}
CHECKED = {}


class PositionSequencer:
    """ This class will act as a generator yielding all Position (instances) of the
    given Board, starting at the given coordinate (row, col).
    """
    def __init__(self, board, row=0, col=0):
        assert Position(row, col) in board, "Position out of range"
        self.max_row = board.n_rows
        self.max_col = board.n_cols
        self.i = row
        self.j = col

    def __iter__(self):
        return self

    def __next__(self):
        """
        :yields: the next position pair
        """
        if self.j >= self.max_col:
            self.j = 0
            self.i += 1

        if self.i >= self.max_row:
            raise StopIteration

        current = Position(self.i, self.j)
        self.j += 1
        return current


def place_pieces(board, pieces, row=0, col=0):
    for pos in PositionSequencer(board, row, col):
        if board[pos.row][pos.col] is not Empty or pos in board.attacked:
            continue

        board_ = board.copy()
        current_pieces = board_.pieces
        board_.place_at(pieces[0], row=i, col=j)
        latest_piece = board_[i][j]

        if len(pieces) == 1:
           yield board  # This is a solution


