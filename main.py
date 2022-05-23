# Code Editing by: Nicolas Zapata Alzate
# UNIR - Fundacion Universitaria Internacional De La Rioja Colombia
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import sys
except:
    print("PyOpenGL not found, Please configure good PyOpenGL")

# Func to draw the cube
def draw():
    xroot = 45
    yroot = 45
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(xroot, 1.0, 0.0, 0.0)
    glRotatef(yroot, 0.0, 1.0, 0.0)
    glutWireCube(0.7) # Create the cube herself
    glFlush()


# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Cube")
glutDisplayFunc(draw)
glutMainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
