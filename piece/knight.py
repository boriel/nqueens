#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Knight']

from .knightmixin import KnightMixIn


class Knight(KnightMixIn):
    """ This does not inherit from any mixin
    """
    def __repr__(self):
        return "N"

    @property
    def attacked_positions(self):
        return self.attacked_knight_positions
