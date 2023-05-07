from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


theta = 10
offsetX = 0
direction = 1


def editProjectionMatrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(20, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)


def editCameraPosition():
    #! position the camera
    gluLookAt(15, 15, 15,  # * eye
              0, 0, 0,     # * center
              0, 1, 0)     # * up vector


def drawMainAxes():
    #! coordinates
    glBegin(GL_LINES)
    #! x-axis
    glColor3d(0, 1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(100, 0, 0)
    #! y-axis
    glColor3d(0, 0, 1)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 100, 0)
    #! z-axis
    glColor3d(1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, 100)
    glEnd()


def drawAxes():
    #! coordinates
    glTranslate(offsetX, 0, 0)
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
    glTranslate(offsetX, 0, 0)
    glTranslate(x, y, z)
    glRotate(-theta, 0, 0, 1)
    # * inner radius, outer radius, longitudes, latitudes
    glutWireTorus(0.15, 0.35, 10, 12)


def drawBulb(x, y, z):
    #! Bulb
    glLoadIdentity()
    editCameraPosition()
    glTranslate(offsetX, 0, 0)
    glTranslate(x, y, z)
    glScale(0.2, 3, 3)
    # * radius, longitudes, latitudes
    glutWireSphere(0.1, 10, 10)


def draw():
    global theta, offsetX, direction
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    editCameraPosition()
    drawMainAxes()
    drawAxes()

    #! Upper Cube
    glColor3d(1, 0, 0)
    glLoadIdentity()
    editCameraPosition()
    glTranslate(offsetX, 0, 0)
    glTranslate(0, 0, 0)
    glScale(4, 1, 2)
    glutWireCube(1)

    #! Lower Cube
    glColor3d(1, 0, 0)
    glLoadIdentity()
    editCameraPosition()
    glTranslate(offsetX, 0, 0)
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

    glutSwapBuffers()

    theta = theta + (1 if direction == 1 else -1)
    offsetX = offsetX + (0.01 if direction == 1 else -0.01)
    if offsetX > 5:
        direction = 0
    elif offsetX < -5:
        direction = 1


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 700)
glutCreateWindow(b"Car Program")
#! Projection matrix
editProjectionMatrix()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
