#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Queen']
__doc__ = "I miss you Freddy"


from .diagonalmixin import DiagonalMixIn
from .horivertmixin import HoriVertMixIn


class Queen(DiagonalMixIn, HoriVertMixIn):
    """ Implements the Queen class by joining both mixings
    """
    def __repr__(self):
        return "Q"

    @property
    def attacked_positions(self):
        return self.attacked_horivert_positions.union(self.attacked_diagonal_positions)
