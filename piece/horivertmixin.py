#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .piece import Piece
from position import Direction


class HoriVertMixIn(Piece):
    """ Defines an ABC for a piece that moves vertically or horizontally
    """
    movementLimit = None  # If set to 1, only distance 1 will be considered

    @property
    def attacked_horivert_positions(self):
        result = set()

        for direction in (Direction.North, Direction.South, Direction.East, Direction.West):
            count = 0
            pos = self.position

            while (self.movementLimit is None or count < self.movementLimit) and pos.go(direction) in self.board:
                pos = pos.go(direction)
                result.add(pos)
                count += 1

        return result
