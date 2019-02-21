from OpenGL.GL import *

class Ground():

    def __init__(self):
        self.ground_vertices = (
            (-20, -0.1, 50),
            (20, -0.1, 50),
            (-20, -0.1, -300),
            (20, -0.1, -300),
        )

    def draw(self):

        glPushMatrix()
        glBegin(GL_QUADS)
        x = 0
        for vertex in self.ground_vertices:
            x += 1
            glColor3fv((0.78,0.55,0.75))
            glVertex3fv(vertex)
        glEnd()
        glPopMatrix()
