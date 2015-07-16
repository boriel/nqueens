#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .piece import Piece
from position import Direction


class DiagonalMixIn(Piece):
    """ Implements the Diagonal movements
    """
    movementLimit = None  # If set to 1, only distance 1 will be considered

    @property
    def attacked_diagonal_positions(self):
        result = set()

        for direction in (Direction.NorthEast, Direction.SouthEast, Direction.NorthWest, Direction.SouthWest):
            count = 0
            pos = self.position

            while (self.movementLimit is None or count < self.movementLimit) and pos.go(direction) in self.board:
                pos = pos.go(direction)
                result.add(pos)

        return result
