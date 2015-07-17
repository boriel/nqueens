#!/usr/bin/env python
# -*- coding: utf-8 -*-


from piece import Piece
from position import Direction

class KnightMixIn(Piece):
    """ This MixIn implements the Knight movement
    """

    @property
    def attacked_knight_positions(self):
        result = set()

        for dirA in (Direction.North, Direction.South, Direction.East, Direction.West):
            posA = self.position.go(dirA).go(dirA)
            for dirB in (
                    Direction.North,
                    Direction.South
            ) if dirA in (Direction.East, Direction.West) else (
                    Direction.East, Direction.West
            ):
                posB = posA.go(dirB)
                if posB in self.board:
                    result.add(posB)

        return result
