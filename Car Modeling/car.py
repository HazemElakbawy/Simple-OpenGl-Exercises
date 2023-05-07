from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def editProjectionMatrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(20, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)


def editCameraPosition():
    #! position the camera
    gluLookAt(10, 10, 10,  # * eye
              0, 0, 0,     # * center
              0, 1, 0)     # * up vector


def drawAxes():
    #! coordinates
    glBegin(GL_LINES)
    #! x-axis
    glColor3d(1, 1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(100, 0, 0)
    #! y-axis
    glColor3d(0, 1, 1)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 100, 0)
    #! z-axis
    glColor3d(1, 0, 1)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, 100)
    glEnd()


def drawWheels(x, y, z):
    #! Wheels
    glLoadIdentity()
    editCameraPosition()
    glTranslate(x, y, z)
    # * inner radius, outer radius, longitudes, latitudes
    glutWireTorus(0.15, 0.35, 10, 12)


def drawBulb(x, y, z):
    #! Bulb
    glLoadIdentity()
    editCameraPosition()
    glTranslate(x, y, z)
    glScale(0.2, 3, 3)
    # * radius, longitudes, latitudes
    glutWireSphere(0.1, 10, 10)


def draw():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    editCameraPosition()
    drawAxes()

    #! Upper Cube
    glColor3d(1, 0, 0)
    glLoadIdentity()
    editCameraPosition()
    glTranslate(0, 0, 0)
    glScale(4, 1, 2)
    glutWireCube(1)

    #! Lower Cube
    glColor3d(1, 0, 0)
    glLoadIdentity()
    editCameraPosition()
    glTranslate(0, 0.85, 0)
    glScale(2, 0.7, 1.5)
    glutWireCube(1)

    #! Wheels
    glColor3d(0, 0, 1)
    drawWheels(2,  -0.5, 1)   # * front left
    drawWheels(2,  -0.5, -1)  # * front right
    drawWheels(-2, -0.5, 1)   # * back left
    drawWheels(-2, -0.5, -1)  # * back right

    #! Bulbs
    glColor3d(1, 1, 0)
    drawBulb(2, 0, -0.45)  # * front left
    drawBulb(2, 0, 0.45)   # * front right

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Car Program")
#! Projection matrix
editProjectionMatrix()
glutDisplayFunc(draw)
# glutIdleFunc(draw)
glutMainLoop()
