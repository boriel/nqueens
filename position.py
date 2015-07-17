#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum


class Direction(Enum):
    North = 1
    South = 2
    East = 4
    West = 8
    NorthEast = 5
    NorthWest = 9
    SouthEast = 6
    SouthWest = 10


class Position:
    """ Defines a position object
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return "%s(row=%i, col=%i)" % (self.__class__.__name__, self.row, self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        return self.row < other.row or (self.row == other.row and self.col < other.col)

    def __hash__(self):
        return hash((self.row, self.col))

    # N, S, W, E properties to get relative positions
    @property
    def North(self):
        """
        :return: A Position north of this one
        """
        return Position(self.row - 1, self.col)

    @property
    def South(self):
        """
        :return: A Position south of this one
        """
        return Position(self.row + 1, self.col)

    @property
    def East(self):
        """
        :return: A Position east of this one
        """
        return Position(self.row, self.col - 1)

    @property
    def West(self):
        """
        :return: A Position west of this one
        """
        return Position(self.row, self.col + 1)

    @property
    def NorthEast(self):
        return self.North.East

    @property
    def SouthEast(self):
        return self.South.East

    @property
    def NorthWest(self):
        return self.North.West

    @property
    def SouthWest(self):
        return self.South.West

    # Short forms are functions, so they can be lazy ;-)
    def N(self):
        return self.North

    def S(self):
        return self.South

    def E(self):
        return self.East

    def W(self):
        return self.West

    def NE(self):
        return self.NorthEast

    def NW(self):
        return self.NorthWest

    def SE(self):
        return self.SouthEast

    def SW(self):
        return self.SouthWest

    # Generic function which accept direction as a paremeter
    def go(self, direction):
        """ Returns a new position going in one of the 8 directions
        :param direction: a Direction.{N,S,W,E...} instance
        :return: the new Position
        """
        assert isinstance(direction, Direction)
        return {
            Direction.North: self.N,
            Direction.South: self.S,
            Direction.East: self.E,
            Direction.West: self.W,
            Direction.NorthEast: self.NE,
            Direction.NorthWest: self.NW,
            Direction.SouthEast: self.SE,
            Direction.SouthWest: self.SW
        }[direction]()
