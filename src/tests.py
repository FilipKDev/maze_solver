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

if __name__ == "__main__":
    unittest.main()