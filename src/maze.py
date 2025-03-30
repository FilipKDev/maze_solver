from graphics import Line, Point
import time

class Cell:
    def __init__(self, window_instance, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window_instance

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def get_centre(self):
        width = (self._x2 - self._x1)
        centre_x = self._x1 + (0.5 * width)
        height = (self._y2 - self._y1)
        centre_y = self._y1 + (0.5 * height)
        return (centre_x, centre_y)

    def draw(self, x1, y1, x2, y2, cell_colour = "black"):
        if self._win is None: 
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, cell_colour)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, cell_colour)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, cell_colour)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, cell_colour)

    def draw_path(self, target_cell, undo=False):
        cell_centre = self.get_centre()
        target_centre = target_cell.get_centre()
        if undo:
            self._win.draw_line(Line(Point(cell_centre[0], cell_centre[1]), Point(target_centre[0], target_centre[1])), "grey")
        else:
            self._win.draw_line(Line(Point(cell_centre[0], cell_centre[1]), Point(target_centre[0], target_centre[1])), "red")

class Maze:
    def __init__(
            self,
            start_x,
            start_y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window_instance = None,
    ):
        self.start_x = start_x
        self.start_y = start_y

        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._win = window_instance
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

        
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self.start_x + (i * self._cell_size_x)
        cell_y1 = self.start_y + (j * self._cell_size_y)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        Cell(self._win).draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)