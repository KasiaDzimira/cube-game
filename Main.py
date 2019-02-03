import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

ground_surfaces = (0, 1, 2, 3)

ground_vertices = (
    (-10, -0.1, 50),
    (10, -0.1, 50),
    (-10, -0.1, -300),
    (10, -0.1, -300),

)

def Ground():
    glBegin(GL_QUADS)

    x = 0
    for vertex in ground_vertices:
        x += 1
        glColor3fv((0, 0.25, 0.25))
        glVertex3fv(vertex)

    glEnd()


def Player(new_vertices):
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv((0, 0.3, 1))
            glVertex3fv(new_vertices[vertex])

    glEnd()

def set_vertices(x_value, y_value, z_value):
    x_value_change = x_value - 1
    y_value_change = y_value
    z_value_change = z_value

    new_vertices = []
    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def get_vertices(vertex_array):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for vert in vertex_array:
        sum_x += vert[0]
        sum_y += vert[1]
        sum_z += vert[2]

    x = sum_x / len(vertex_array) + 1
    y = sum_y / len(vertex_array)
    z = sum_z / len(vertex_array)

    return [x, y, z]

def Cubes(new_vertices):
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(new_vertices[vertex])

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)
    glTranslatef(random.randrange(-5, 5), 0, 0)

    x_move = 0
    y_move = 0
    player_move_x = 0
    player_move_z = 0

    cube_dict = {}
    x_value = -4
    z_value = -20
    y_value = 0

    cube_dict[0] = set_vertices(-5, 0, -20)

    for x in range(7):
        x_value = x_value + 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(8, 12):
        z_value = z_value - 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(13, 14):
        y_value = y_value + 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(15, 18):
        z_value = z_value - 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(19, 21):
        x_value = x_value - 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(22, 23):
        y_value = y_value + 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(24, 27):
        z_value = z_value - 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    for x in range(28, 30):
        y_value = y_value + 2
        cube_dict[x] = set_vertices(x_value, y_value, z_value)

    object_passed = False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3

                if event.key == pygame.K_RIGHT:
                    x_move = -0.3

                if event.key == pygame.K_UP:
                    y_move = -0.3

                if event.key == pygame.K_DOWN:
                    y_move = 0.3

                if event.key == pygame.K_w:
                    player_move_z = -0.2

                if event.key == pygame.K_s:
                    player_move_z = 0.2
                
                if event.key == pygame.K_a:
                    player_move_x = -0.2

                if event.key == pygame.K_d:
                    player_move_x = 0.2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_move = 0

                if event.key == pygame.K_RIGHT:
                    x_move = 0

                if event.key == pygame.K_UP:
                    y_move = 0

                if event.key == pygame.K_DOWN:
                    y_move = 0

                if event.key == pygame.K_w:
                    player_move_z = 0

                if event.key == pygame.K_s:
                    player_move_z = 0
                
                if event.key == pygame.K_a:
                    player_move_x = 0

                if event.key == pygame.K_d:
                    player_move_x = 0

        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        glTranslatef(x_move, y_move, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Ground()
        for each_cube in cube_dict:
            Cubes(cube_dict[each_cube])

        current_player_pos = get_vertices(cube_dict[0])
        new_pos_x = current_player_pos[0] + player_move_x
        new_pos_y = current_player_pos[1]
        new_pos_z = current_player_pos[2] + player_move_z
        cube_dict[0] = set_vertices(new_pos_x, new_pos_y, new_pos_z)
        Player(cube_dict[0])
        pygame.display.flip()

main()