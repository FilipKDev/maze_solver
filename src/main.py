from maze import Maze
from graphics import Window
import sys

def main():
    sys.setrecursionlimit(10000)
    win = Window(1080, 1080)
    maze = Maze(50, 50, 15, 15, 25, 25, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    win.wait_for_close()

main()