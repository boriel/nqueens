#!/usr/bin/env python
# -*- coding: utf-8 -*-


__doc__ = """ Defines a generic Abstract Base Class for every piece.
          """

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
from collections import namedtuple

Position = namedtuple('Position', ('col', 'row'))


class Piece(metaclass=ABCMeta):
    """ Implements the Abstract Base Class for any piece
    """
    def __init__(self, position, board):
        assert isinstance(position, Position)
        self.position = position
        self.board = board

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
