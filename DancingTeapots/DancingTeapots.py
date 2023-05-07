from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

SMALL_CYLINDER_HEIGHT, SMALL_CYLINDER_RADIUS = 2, 0.05
BIG_CYLINDER_HEIGHT, BIG_CYLINDER_RADIUS = 8, 2.5

angles = [0, 80, 150, 230, 300]
offsets = [0, 0.3, 0.3, 0.2, 0]
teapotGoesUp = [0, 0, 1, 0, 1]
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (0.2, 0.5, 0.5)]

angleRate, selfRotation, offsetRate = 0.5, 1, 0.002

offsetFromOrigin = 2
animate = 0

# TODO: write docstring


def adjustProjectionAndCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 2, 100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(4, 2.5, 4,
              0, 0, 0,
              0, 1, 0)
    glEnable(GL_DEPTH_TEST)


def drawMessage():
    glPushMatrix()
    glLineWidth(2)
    glColor3f(1, 0, 0)
    glTranslate(-2.5, 2, 1)
    glRotate(45, 0, 1, 0)
    glScale(0.003, 0.003, 1)
    for ch in b"Press t to toggle animation":
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ch)
    glPopMatrix()


def checkOffset(offset):
    if offset >= 0.25:
        return 0
    elif offset <= -0.35:
        return 1
    else:
        return -1


def editOffset(goUp, offset):
    global offsetRate
    offset += offsetRate if goUp else -offsetRate
    return offset


def drawCylinder(Matrix: list, radius, height):
    glTranslate(Matrix[0], Matrix[1], Matrix[2])
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(radius, height, 30, 30)


def translateTeapot(offset):
    glPushMatrix()
    glTranslate(0, offset, 0)
    glutWireTeapot(0.5)
    glPopMatrix()


def rotateAroundItself(selfRotation, offset):
    # * Rotate Teapots around the cylinder
    glPushMatrix()
    glRotate(selfRotation, 0, 1, 0)
    translateTeapot(offset)
    glColor3f(0.4, 0.3, 0.2)
    drawCylinder([0, offset, 0], SMALL_CYLINDER_RADIUS, SMALL_CYLINDER_HEIGHT)
    glPopMatrix()


def rotateAroundOrigin(angle, offset):
    # * rotate Teapots around origin
    glPushMatrix()
    glRotate(angle, 0, 1, 0)
    glTranslate(offsetFromOrigin, 0, 0)
    rotateAroundItself(selfRotation, offset)
    glPopMatrix()


def createTeapots(angle, offset, colors):
    glColor3f(colors[0], colors[1], colors[2])
    rotateAroundOrigin(angle, offset)


def keyboard(key, x, y):
    global animate
    if key == b't':  # * toggle animation
        animate = 1 - animate
    if key == b's':  # * exit program
        sys.exit(0)


def draw():
    global angles, offsets, teapotGoesUp, selfRotation, colors
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # ! Message
    glColor3f(0.6, 0.4, 0.2)
    drawMessage()

    # ! Big Cylinder
    glPushMatrix()
    glColor3f(1, 1, 1)
    drawCylinder([0.15, -0.8, 0.15], BIG_CYLINDER_RADIUS, BIG_CYLINDER_HEIGHT)
    glPopMatrix()

    #!  Draw Teapots
    for i in range(5):
        createTeapots(angles[i], offsets[i], colors[i])

    #! Check Animation
    if not animate:
        glutSwapBuffers()
        return

    glutSwapBuffers()
    selfRotation += 1

    for i in range(5):
        offsets[i] = editOffset(teapotGoesUp[i], offsets[i])
        if checkOffset(offsets[i]) != -1:
            teapotGoesUp[i] = checkOffset(offsets[i])

    for i in range(5):
        angles[i] += angleRate


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutInitWindowPosition(600, 200)
glutCreateWindow(b"Dancing Teapots")
glutDisplayFunc(draw)
glutKeyboardFunc(keyboard)
glutIdleFunc(draw)
adjustProjectionAndCamera()
glutMainLoop()
