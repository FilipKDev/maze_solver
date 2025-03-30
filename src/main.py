from maze import Maze
from graphics import Window

def main():
    win = Window(960, 540)
    Maze(50, 50, 12, 10, 10, 10, win)
    win.wait_for_close()

main()