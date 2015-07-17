#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Amazon']

__doc__ = """ Implements the Amazon chess piece (not used in this problem)
            See: https://en.wikipedia.org/wiki/Amazon_%28chess%29
          """

from .knightmixin import KnightMixIn
from .queen import Queen

class Amazon(Queen, KnightMixIn):
    """ An Amazon is Queen riding a Horse (Knight)
    """
    def __repr__(self):
        return "A"  # "QN" is the official notation

    @property
    def attacked_positions(self):
        return super().attacked_positions.union(self.attacked_knight_positions)
