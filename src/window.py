from tkinter import Tk, BOTH, Canvas

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
    def __init__(self, x1, y1, x2, y2, window_instance, cell_colour = "black", has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.win = window_instance

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.draw(cell_colour)

    def get_centre(self):
        width = (self._x2 - self._x1)
        centre_x = self._x1 + (0.5 * width)
        height = (self._y2 - self._y1)
        centre_y = self._y1 + (0.5 * height)
        return (centre_x, centre_y)

    def draw(self, cell_colour):
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