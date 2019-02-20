from OpenGL.GL import *

class Player():

    def __init__(self):

        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )

        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )


    def draw(self, new_vertices):
        glBegin(GL_QUADS)

        for surface in self.surfaces:
            x = 0

            for vertex in surface:
                x += 1
                glColor3fv((0.92, 0.68, 0.76))
                glVertex3fv(new_vertices[vertex])
        glEnd()