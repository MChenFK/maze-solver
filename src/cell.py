from constants import *
from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            fill_color = MAZE_WALL_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, fill_color)

        if self.has_right_wall:
            fill_color = MAZE_WALL_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, fill_color)
        
        if self.has_top_wall:
            fill_color = MAZE_WALL_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, fill_color)
        
        if self.has_bottom_wall:
            fill_color = MAZE_WALL_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, fill_color)
        

    def draw_move(self, to_cell, undo=False):
        half1 = abs(self._x2 - self._x1) // 2
        center1 = Point(self._x1 + half1, self._y1 + half1)

        half2 = abs(to_cell._x2 - to_cell._x1) // 2
        center2 = Point(to_cell._x1 + half2, to_cell._y1 + half2)

        line = Line(center1, center2)

        if not undo:
            line_color = MOVE_COLOR
        else:
            line_color = UNDO_COLOR

        self._win.draw_line(line, line_color)