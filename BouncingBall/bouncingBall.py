from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *

x, y = 0.35, -0.2
dirX, dirY = 1, 1
mx = 1
rad = 0.1
animate = 0


def Init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-mx, mx, -mx, mx, -mx, mx)
    glMatrixMode(GL_MODELVIEW)


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
    global x, y, dirX, dirY, animate
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    drawAxes()

    if animate:
        x += 0.01*dirX
        y += 0.01*dirY
        # * Collision detected
        if x > mx-rad or x < -mx+rad:
            dirX = -dirX
        if y > mx-rad or y < -mx+rad:
            dirY = -dirY

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
        sys.exit()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bouncing Ball")
glutDisplayFunc(draw)
glutKeyboardFunc(keyboard)
glutIdleFunc(draw)
Init()
glutMainLoop()
