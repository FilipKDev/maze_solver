from graphics import Line, Point
import time
import random

class Cell:
    def __init__(self, window_instance = None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window_instance

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

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
        else:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "white")

        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, cell_colour)
        else:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "white")

        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, cell_colour)
        else:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, cell_colour)
        else:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "white")

    def draw_path(self, target_cell, undo=False):
        if self._win is None:
            return
        cell_centre = self.get_centre()
        target_centre = target_cell.get_centre()
        if undo:
            self._win.draw_line(Line(Point(cell_centre[0], cell_centre[1]), Point(target_centre[0], target_centre[1])), "white")
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
            seed = None
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

        if seed:
            random.seed(seed)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.00002)

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

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        top_left_cell.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_right_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        if self._cells is None:
            return
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append("left")
            if i + 1 < self._num_cols and not self._cells[i+1][j].visited:
                to_visit.append("right")
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append("up")
            if j + 1 < self._num_rows and not self._cells[i][j+1].visited:
                to_visit.append("down")

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = random.randrange(len(to_visit))
            if to_visit[direction] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            if to_visit[direction] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            if to_visit[direction] == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            if to_visit[direction] == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        start = Cell(self._win)
        start.has_left_wall = False
        start.has_right_wall = False
        start.has_top_wall = False
        start.has_bottom_wall = False
        start.draw(self.start_x, self.start_y - self._cell_size_y, self.start_x + self._cell_size_x, self.start_y)
        start.draw_path(self._cells[0][0])
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            end = Cell(self._win)
            end.has_left_wall = False
            end.has_right_wall = False
            end.has_top_wall = False
            end.has_bottom_wall = False
            end_x1 = self.start_x + ((self._num_cols - 1) * self._cell_size_x)
            end_y1 = self.start_y + ((self._num_rows) * self._cell_size_y)
            end_x2 = self.start_x + (self._num_cols * self._cell_size_x)
            end_y2 = self.start_y + ((self._num_rows + 1) * self._cell_size_y)
            end.draw(end_x1, end_y1, end_x2, end_y2)
            self._cells[i][j].draw_path(end)
            return True
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for direction in directions:
            col = direction[0]
            row = direction[1]
            if 0 <= col < self._num_cols and 0 <= row < self._num_rows:
                if self._cells[col][row] and not self._cells[col][row].visited:
                    if col == i - 1 and not self._cells[i][j].has_left_wall:
                        self._cells[i][j].draw_path(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        self._cells[i][j].draw_path(self._cells[col][row], True)
                    if col == i + 1 and not self._cells[i][j].has_right_wall:
                        self._cells[i][j].draw_path(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        self._cells[i][j].draw_path(self._cells[col][row], True)
                    if row == j - 1 and not self._cells[i][j].has_top_wall:
                        self._cells[i][j].draw_path(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        self._cells[i][j].draw_path(self._cells[col][row], True)
                    if row == j + 1 and not self._cells[i][j].has_bottom_wall:
                        self._cells[i][j].draw_path(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        self._cells[i][j].draw_path(self._cells[col][row], True)
        return False