# maze-solver

GUI maze solver built using Python and Tkinter
- Given a margin size, number of columns and rows, and cell size, generates and solves a maze
- Maze is displayed using a Tkinter canvas and update methods to continuously render changes to the walls and solve path

## src
### constants.py
Contains constant values for animation sleep and background / line colors

### main.py
Generates and solves maze using functions from maze.py

### graphics.py
Contains classes for the window, points and lines

### cell.py
Contains functions to draw cells to window

### maze.py
Contains functions to generate and solve the maze

### tests.py
Contains unit tests for creating maze and reseting visited cell flags
