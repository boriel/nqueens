# README #

## The N-Pieces Chess Challenge ##

This repo contains the source code for the N-Pieces Chess Challenge problem.
The challenge is to put N pieces on an MxN chessboard so no piece is attacked by any other.
All possible combinations must be obtained.

* Version 1.0
* Language: Python 3.x

## Installation and Usage ##

Other than a python 3.x interpreter, nothing extra is required in your system.
To run it just type:

```
#!bash

python main.py 
```
Then you can type a sentence to specify the configuration to solve, like:
_3x3 Board containing 2 Kings and 1 Rook._

The program does a (very) naive parsing to understand the board size and pieces in plain English.
You can also read from standard input.

### Code ###

#### Design ####

* The folder testing/ contains the TDD cases. Read below.
* The folder piece/ is a python package containing the piece class hierarchy.

#### Classes ####

* The **Piece** class is the an Abstract Base Class (ABC) from which all other classes derive.
* **DiagonalMixIn** implements the diagonal movement (Queen, Bishop). 
This movement can be limited to 1 step (for the King).
* **HoriVertMixIn** implements the horizontal movement (Queen, Rook).
This movement can be limited to 1 step (for the King).
* **KnightMixIn** implements the knight movement (Knight and a fictional piece, Amazon, not used here).

![class_diagram.jpg](https://bitbucket.org/repo/rzroxR/images/4135032722-class_diagram.jpg)

### Algorithm ###

The algorithm does a recursive deep-first iteration, and it's encapsulated within an iterable
class for better legibility.

### Code Testing ###

Test suite used is nose compatible. All test are located within the tests/ folder.
Every class has its own tests to ensure minimal functionality.
A coverage report is also included in the folder /tests/coverage (open index.html with a 
web browser). Coverage is nearly 100% (classes in main.py not included).

### Who do I talk to? ###
[Jose Rodriguez](http://boriel.com) ([@boriel](http://www.twitter.com/boriel))