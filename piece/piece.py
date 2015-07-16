#!/usr/bin/env python
# -*- coding: utf-8 -*-


__doc__ = """ Defines a generic Abstract Base Class for every piece.
          """

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty

from position import Position


class Piece(metaclass=ABCMeta):
    """ Implements the Abstract Base Class for any piece
    """
    def __init__(self, position, board):
        self.position = position
        self.board = board

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        assert isinstance(position, Position)
        self._position = position

    @abstractmethod
    def __repr__(self):
        pass

    @abstractproperty
    def attacked_positions(self):
        """
        :return: A python set of Position instances reachable by this piece.
        """
        pass

    def can_attack(self, position):
        return position in self.attacked_positions

    def move_to(self, row, col):
        """ Places the piece in the new location, checking it is in range
        :param row: Board row (0..max_row - 1)
        :param col: Board col (0..max_col - 1)
        """
        self.position = Position(row, col)

