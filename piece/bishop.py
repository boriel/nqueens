#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .diagonalMixIn import DiagonalMixIn

class Bishop(DiagonalMixIn):
    """ Implements the Bishop class
    """

    def __repr__(self):
        return "B"

    @property
    def attacked_positions(self):
        return self.attacked_diagonal_positions
