from graphics import *
from math import atan2, sin, cos, pi, sqrt

win = GraphWin('Field', 700, 700)
NUM_LINES = 26
SPACE = 700/NUM_LINES

offset1X = 2
offset1Y = 4
offset2X = -4
offset2Y = -4

c1 = Circle(Point(350 + SPACE*offset1X, 350 + SPACE*offset1Y), 20)
c1.setFill("red")
c1.draw(win)

c2 = Circle(Point(350 + SPACE*offset2X, 350 + SPACE*offset2Y), 20)
c2.setFill("red")
c2.draw(win)

for x in range(0, NUM_LINES):
    line = Line(Point(0, SPACE*x), Point(700, SPACE*x))
    line.draw(win)

for y in range(0, NUM_LINES):
    line = Line(Point(SPACE*y, 0), Point(SPACE*y, 700))
    line.draw(win)

NLD2 = int(NUM_LINES/2) + 1
for x in range(-NLD2, NLD2):
    for y in range(-NLD2, NLD2):
        try:
            i = (1500/((x-offset1X)**2 + (y+offset1Y)**2))*cos(atan2(y+offset1Y, x-offset1X))
            i += (1500/((x-offset2X)**2 + (y+offset2Y)**2))*cos(atan2(y+offset2Y, x-offset2X))
        except:
            i = 0
        try:
            j = (1500/((x-offset1X)**2 + (y+offset1Y)**2))*sin(atan2(y+offset1Y, x-offset1X))
            j += (1500/((x-offset2X)**2 + (y+offset2Y)**2))*sin(atan2(y+offset2Y, x-offset2X))
        except:
            j = 0

        lenx = (SPACE/75)*i
        leny = (SPACE/75)*j

        startx = 350 + x*SPACE
        starty = 350 - y*SPACE
        endx = startx + lenx
        endy = starty - leny

        angle = atan2(starty - endy, endx - startx)

        arrow1 = Line(Point(startx, starty), Point(endx, endy))
        arrow2 = Line(Point(endx+(SPACE/5)*sin(angle - 3*pi/8), endy+(SPACE/5)*cos(angle - 3*pi/8)), Point(endx, endy))
        arrow3 = Line(Point(endx+(SPACE/5)*sin(angle - 5*pi/8), endy+(SPACE/5)*cos(angle - 5*pi/8)), Point(endx, endy))
        arrow1.draw(win)
        arrow2.draw(win)
        arrow3.draw(win)

win.getMouse()
