from OpenGL.GL import *

def resize(width, height):

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    
    glEnable(GL_DEPTH_TEST)

    # background is opaque black
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def drawGLRect(size):

    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex(-size/2, -size/2, 0)
    glTexCoord(1, 0)
    glVertex(size/2, -size/2, 0)
    glTexCoord(1, 1)
    glVertex(size/2, size/2, 0)
    glTexCoord(0, 1)
    glVertex(-size/2, size/2, 0)
    glEnd()
