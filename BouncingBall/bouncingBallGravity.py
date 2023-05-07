from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *

mx = 1
rad = 0.1
x, y = 0.35, -0.2
horizontalVelocity, verticalVelocity = 1, 3
time = 0.005
animate = 0


def Init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-mx, mx, -mx, mx, -mx, mx)
    glMatrixMode(GL_MODELVIEW)


def drawBorders():
    glBegin(GL_LINE_STRIP)
    glColor3d(1, 1, 1)
    glVertex3d(-mx+0.001, -mx+0.001, 0)
    glVertex3d(-mx+0.001, mx-0.001, 0)
    glVertex3d(mx-0.001, mx-0.001, 0)
    glVertex3d(mx-0.001, -mx+0.001, 0)
    glVertex3d(-mx+0.001, -mx+0.001, 0)
    glEnd()

def drawAxes():
    glBegin(GL_LINES)
    # * x axis
    glColor3d(1, 0, 0)
    glVertex3d(-1, 0, 0)
    glVertex3d(1, 0, 0)
    # * y axis
    glColor3d(0, 1, 0)
    glVertex3d(0, -1, 0)
    glVertex3d(0, 1, 0)
    glEnd()


def draw():
    global x, y, horizontalVelocity, verticalVelocity, animate
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    drawBorders()
    drawAxes()

    if animate:
        x = x + horizontalVelocity * time
        verticalVelocity = verticalVelocity - 9.8 * time
        y = y + verticalVelocity * time

        # * Collision detected
        if x > mx-rad or x < -mx+rad:
            horizontalVelocity *= -1
        if y > mx-rad or y < -mx+rad:
            verticalVelocity *= -1

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x, y, -1)
    glutSolidSphere(rad, 20, 20)

    glutSwapBuffers()


def keyboard(key, x, y):
    global animate
    if key == b"t":  # * toggle animation
        animate = 1 - animate
    if key == b"q":
        sys.exit(0)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bouncing Ball")
glutDisplayFunc(draw)
glutKeyboardFunc(keyboard)
glutIdleFunc(draw)
Init()
glutMainLoop()
