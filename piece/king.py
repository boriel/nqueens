#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .queen import Queen


class King(Queen):
    """ A king is like a queen, but just can move 1 square
    """
    movementLimit = 1

    def __repr__(self):
        return "K"

