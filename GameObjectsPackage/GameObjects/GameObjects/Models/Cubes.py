from OpenGL.GL import *
class Cubes():

    def __init__(self):
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
        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )
        self.colors = (
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
            (0.22, 0.68, 0.76),
        )


    def set_vertices(self, x_value, y_value, z_value):
        x_value_change = x_value - 1
        y_value_change = y_value
        z_value_change = z_value

        new_vertices = []
        for vert in self.vertices:
            new_vert = []

            new_x = vert[0] + x_value_change
            new_y = vert[1] + y_value_change
            new_z = vert[2] + z_value_change

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)

            new_vertices.append(new_vert)

        return new_vertices

    def draw(self,new_vertices):
        glBegin(GL_QUADS)

        for surface in self.surfaces:
            x = 0

            for vertex in surface:
                if surface == self.surfaces[4]:
                    glColor3fv([0.27, 0.55, 0.6])
                else:
                    glColor3fv(self.colors[x])
                glVertex3fv(new_vertices[vertex])

        glEnd()