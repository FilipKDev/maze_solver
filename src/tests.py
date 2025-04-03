import unittest
from maze import Maze

class Maze_Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze_1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze_1._cells),
            num_cols
        )
        self.assertEqual(
            len(maze_1._cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        maze_1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze_1._break_entrance_and_exit()
        top_left_cell = maze_1._cells[0][0]
        bottom_right_cell = maze_1._cells[num_cols-1][num_rows-1]
        self.assertEqual(
            top_left_cell.has_top_wall,
            False
        )
        self.assertEqual(
            bottom_right_cell.has_bottom_wall,
            False
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 6
        num_rows = 6
        maze_1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze_1._break_entrance_and_exit()
        maze_1._break_walls_r(0, 0)
        maze_1._reset_cells_visited()
        for column in maze_1._cells:
            for cell in column:
                self.assertEqual(
                    cell.visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()