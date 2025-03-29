from window import Window
from window import Line
from window import Point

def main():
    win = Window(800, 600)
    line_1 = Line(Point(10, 10), Point(10, 60))
    line_2 = Line(Point(10, 10), Point(60, 10))
    line_3 = Line(Point(60, 10), Point(60, 60))
    line_4 = Line(Point(60, 60), Point(10, 60))
    win.draw_line(line_1, "black")
    win.draw_line(line_2, "red")
    win.draw_line(line_3, "blue")
    win.draw_line(line_4, "green")
    win.wait_for_close()

main()