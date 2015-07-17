#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Rook']

from .horivertmixin import HoriVertMixIn


class Rook(HoriVertMixIn):
    """ Implements the Rook class
    """

    def __repr__(self):
        return "R"

    @property
    def attacked_positions(self):
        return self.attacked_horivert_positions

