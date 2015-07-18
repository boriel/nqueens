#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board import Board, Empty
from piece import King, Queen, Rook, Bishop, Knight, Piece
from position import Position

import re


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


class ValidBoards:
    """ This class implements an iterator over all valid board configurations.
    """
    def __init__(self, board, piece_types):
        """
        :param board: A board object. E.g. Board(5, 5)
        :param piece_types: An iterable of Piece classes (e.g. [King, King, Rook])
        """
        assert isinstance(board, Board), "board must be a Board instance"
        assert all(issubclass(piece_type, Piece) for piece_type in piece_types)
        self.board = board
        self.piece_types = piece_types

    def __iter__(self):
        yield from self._valid_boards(self.board, self.piece_types, 0, 0)

    def _valid_boards(self, board, pieces, row, col):
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
                yield from self._valid_boards(board_, pieces[1:], next_row, next_col)


class InputParser:
    """ Implements a (very) simple parser using Regular Expressions,
    to parse sentences like "4×4 board containing 2 Rooks and 4 Knights"
    """
    piece_names = {
        'king': King,
        'queen': Queen,
        'rook': Rook,
        'knight': Knight,
        'bishop': Bishop
    }

    class SizeNotSpecifiedError(Exception):
        def __str__(self):
            return "Board size not specified"

    class PiecesNotSpecifiedError(Exception):
        def __str__(self):
            return "No pieces specified"

    def __init__(self, string):
        """
        :param string: String to parse
        """
        string = string.lower()

        size_RE = re.compile(r'(\d+x\d+)[ \t]board')
        parse_size = size_RE.search(string)
        if parse_size is None:
            raise InputParser.SizeNotSpecifiedError
        self.M, self.N = tuple(int(x) for x in parse_size.groups()[0].split('x'))
        pieces_RE = re.compile(r'(\d+[ \t]+(?:%s))' %
                               '|'.join(x.__name__ for x in self.piece_names.values()), re.IGNORECASE)
        pieces_list = pieces_RE.findall(string)
        if not pieces_list:
            raise InputParser.PiecesNotSpecifiedError

        self.pieces_list = [self.piece_names[piece] for n, piece_type in [re.split('[ \t+]', x) for x in pieces_list]
                            for piece in int(n) * [piece_type]]

def main():
    parser = InputParser(input())
    for board in ValidBoards(Board(parser.M, parser.N), parser.pieces_list):
        print(board)

# Example input: 3x3 board containing 2 Kings and 1 Rook.
if __name__ == '__main__':
    main()
