from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


theta = 0
offset = 0
direction = 1


def editProjectionMatrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
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


def drawWheels(x, y, z, theta):
    #! Wheels
    glPushMatrix()
    glTranslate(x, y, z)
    glRotate(theta, 0, 0, -1)
    # * inner radius, outer radius, longitudes, latitudes
    glutWireTorus(0.15, 0.35, 10, 12)
    glPopMatrix()


def drawBulb(x, y, z):
    #! Bulb
    glPushMatrix()
    glTranslate(x, y, z)
    glScale(0.2, 3, 3)
    # * radius, longitudes, latitudes
    glutWireSphere(0.1, 10, 10)
    glPopMatrix()


def drawCar(theta):
    #! Upper Cube
    glColor3d(1, 0, 0)
    glPushMatrix()
    glScale(4, 1, 2)
    glutWireCube(1)
    glPopMatrix()

    #! Lower Cube
    glPushMatrix()
    glTranslate(0, 0.85, 0)
    glScale(2, 0.7, 1.5)
    glutWireCube(1)
    glPopMatrix()

    #! Wheels
    glColor3d(0, 0, 1)
    drawWheels(2,  -0.5, 1, theta)   # * front left
    drawWheels(2,  -0.5, -1, theta)  # * front right
    drawWheels(-2, -0.5, 1, theta)   # * back left
    drawWheels(-2, -0.5, -1, theta)  # * back right

    #! Bulbs
    glColor3d(1, 1, 0)
    drawBulb(2, 0, -0.45)  # * front left
    drawBulb(2, 0, 0.45)   # * front right


def draw():
    global theta, offset, direction
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawAxes()

    # * rotate around y-axis then translate on z-axis
    # !Note: -1 used instead of 1 to rotate in opposite direction
    glPushMatrix()
    glTranslate(0, 0, offset)
    glRotate(90, 0, -1, 0)
    drawCar(theta)
    glPopMatrix()

    # * normal movement in x-axis
    glPushMatrix()
    glTranslate(offset, 0, 0)
    drawCar(theta)
    glPopMatrix()

    # * rotate around z-axis then translate on x-axis
    # !Note: -1 used instead of 1 to rotate in opposite direction
    glPushMatrix()
    glTranslate(0, offset, 0)
    glRotate(90, 0, 0, 1)
    drawCar(theta)
    glPopMatrix()

    glutSwapBuffers()

    theta = theta + (0.5 if direction else -0.5)
    offset = offset + (0.01 if direction else -0.01)
    if offset >= 5:
        direction = 0
    elif offset <= -5:
        direction = 1


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 700)
glutCreateWindow(b"Car Program")
glutInitWindowPosition(1200, 200)
editProjectionMatrix()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
