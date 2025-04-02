from maze import Maze
from graphics import Window

def main():
    win = Window(960, 540)
    maze = Maze(50, 50, 10, 10, 15, 15, win)
    maze._break_entrance_and_exit()
    win.wait_for_close()

main()