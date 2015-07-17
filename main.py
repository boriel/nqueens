#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board import Board, Empty
from piece import King, Queen, Rook, Bishop, Knight
from position import Position

M, N = 3, 3
pieces = [King, King, Rook]


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
    occupied = {piece.position for piece in board.pieces}

    for pos in PositionSequencer(board, row, col):
        if board.at(pos) is not Empty or pos in board.attacked:
            continue

        board_ = board.copy()
        board_.place(pieces[0], pos)

        if occupied.intersection(board_.at(pos).attacked_positions):
            continue  # not valid. The new piece is attacking previous ones

        if len(pieces) == 1:
            yield board_  # This is a solution
        else:
            if pieces[0] is pieces[1]:  # The same type of piece?
                next_row, next_col = pos.row, pos.col
            else:
                next_row, next_col = 0, 0

            yield from place_pieces(board_, pieces[1:], next_row, next_col)


def main(*args, **kwargs):
    for board in place_pieces(Board(M, N), [King, King, Rook]):
        print(board)


if __name__ == '__main__':
    main()
