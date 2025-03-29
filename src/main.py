from window import Window
from window import Cell

def main():
    win = Window(960, 540)
    cell_1 = Cell(100, 100, 200, 200, win, "black", False, True, True, False)
    cell_2 = Cell(100, 200, 200, 300, win, "black", True, True, False, False)
    cell_3 = Cell(100, 300, 200, 400, win, "black", True, True, False, False)
    cell_4 = Cell(100, 400, 200, 500, win, "black", True, False, False, True)
    cell_1.draw_path(cell_2)
    cell_2.draw_path(cell_3)
    cell_3.draw_path(cell_4)

    Cell(200, 100, 300, 200, win, "black", True, False, True, False)
    Cell(200, 200, 300, 300, win, "black", True, True, False, False)
    Cell(200, 300, 300, 400, win, "black", True, True, False, False)
    Cell(200, 400, 300, 500, win, "black", False, True, False, True)
    win.wait_for_close()

main()