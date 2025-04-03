from maze import Maze
from graphics import Window

def main():
    win = Window(960, 540)
    maze = Maze(50, 50, 10, 10, 40, 40, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    win.wait_for_close()

main()