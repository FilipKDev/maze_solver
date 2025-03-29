from window import Window, Cell, Maze

def main():
    win = Window(960, 540)
    Maze(50, 50, 10, 10, 60, 30, win)
    win.wait_for_close()

main()