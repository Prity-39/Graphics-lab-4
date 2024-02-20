#------------Prity(39)-------------

import glfw
from OpenGL.GL import *
import math

W, H = 800, 600

colors= [[255,255,255],
[255,0,0],
[0,255,0],
[0,0,255],
[255,255,0],
[0,255,255],
[255,0,255],
[127,127,127]]


def draw_axes():
    glColor3ub(127, 127, 127)
    glBegin(GL_LINES)
    glVertex2f(-W/2, 0)
    glVertex2f(W/2-1, 0)
    glVertex2f(0, -H/2)
    glVertex2f(0, H/2-1)
    glEnd()

def draw_pixel(x, y):
    glVertex2f(x, y)

def draw8way(xc, yc, x, y):
    draw_pixel(xc + x, yc + y);
    draw_pixel(xc - x, yc + y);
    draw_pixel(xc + x, yc - y);
    draw_pixel(xc - x, yc - y);
    draw_pixel(xc + y, yc + x);
    draw_pixel(xc - y, yc + x);
    draw_pixel(xc + y, yc - x);
    draw_pixel(xc - y, yc - x);
    
#for R1
def drawCircle(r, xc, yc):
    d =4*(5/4-r)
    x = 0
    y = r

    while x <= y:
        if(d > 0):
            y = y - 1
            d += 4*(2*(x - y) + 5)
        else:
            d += 4*(2*x + 3)
        x = x + 1
        print(x, y)
        draw8way(xc, yc, x, y)
    
def myEvent(): 
    glBegin(GL_POINTS)
    drawCircle(r, xc, yc)
    glEnd()



def main():
    # Initialize GLFW
    if not glfw.init():
        return

    W, H = 800, 600

    # Take input values for r, xc, and yc
    r = int(input("Enter the radius (r) of the circle: "))
    xc = int(input("Enter the x-coordinate (xc) of the center: "))
    yc = int(input("Enter the y-coordinate (yc) of the center: "))

    Window = glfw.create_window(W, H, "Lab 4 by roll 39", None, None)
    if not Window:
        glfw.terminate()
        return

    glfw.make_context_current(Window)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Set up the orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W/2, W/2-1, -H/2, H/2-1, -1,1)
    
    # Set up to use the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_axes() # Vertical and Horizontal Line

    # Draw the circle with the input values
    glBegin(GL_POINTS)
    drawCircle(r, xc, yc)
    glEnd()

    glfw.swap_buffers(Window)
    glfw.poll_events()

    while not glfw.window_should_close(Window):
        glfw.wait_events()

    glfw.terminate()

main()