from maze import Maze
from graphics import Window
import sys

def main():
    sys.setrecursionlimit(10000)
    win = Window(1800, 1800)
    maze = Maze(50, 50, 25, 25, 50, 50, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

main()