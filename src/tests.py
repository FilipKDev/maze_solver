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

if __name__ == "__main__":
    unittest.main()