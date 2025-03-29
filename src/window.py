from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title = "Window"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(width = self.width, height = self.height)
        self.canvas.pack()
        
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_colour, width=2
        )

class Cell:
    def __init__(self, window_instance, x1 = None, y1 = None, x2 = None, y2 = None, cell_colour = "black", has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.win = window_instance

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        if self.can_draw():
            self.draw(cell_colour)

    def can_draw(self):
        return self._x1 and self._y1 and self._x2 and self._y2

    def get_centre(self):
        width = (self._x2 - self._x1)
        centre_x = self._x1 + (0.5 * width)
        height = (self._y2 - self._y1)
        centre_y = self._y1 + (0.5 * height)
        return (centre_x, centre_y)

    def draw(self, cell_colour):
        if not self.can_draw():
            return
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.win.draw_line(left_wall, cell_colour)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.win.draw_line(right_wall, cell_colour)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.win.draw_line(top_wall, cell_colour)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.win.draw_line(bottom_wall, cell_colour)

    def draw_path(self, target_cell, undo=False):
        cell_centre = self.get_centre()
        target_centre = target_cell.get_centre()
        if undo:
            self.win.draw_line(Line(Point(cell_centre[0], cell_centre[1]), Point(target_centre[0], target_centre[1])), "grey")
        else:
            self.win.draw_line(Line(Point(cell_centre[0], cell_centre[1]), Point(target_centre[0], target_centre[1])), "red")

class Maze:
    def __init__(
            self,
            start_x,
            start_y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window_instance,
    ):
        self.start_x = start_x
        self.start_y = start_y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window_instance
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

        
    def _draw_cell(self, i, j):
        cell_x1 = self.start_x + (i * self.cell_size_x)
        cell_y1 = self.start_y + (j * self.cell_size_y)
        cell_x2 = self.start_x + ((i+1) * self.cell_size_x)
        cell_y2 = self.start_y + ((j+1) * self.cell_size_y)

        Cell(self.win, cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)