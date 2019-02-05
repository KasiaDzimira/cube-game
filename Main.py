import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from math import floor, ceil

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
    (-20, -0.1, 50),
    (20, -0.1, 50),
    (-20, -0.1, -300),
    (20, -0.1, -300),

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

def check_collision(pos1, pos2):
    x_diff = abs(pos1[0] - pos2[0])
    y_diff = abs(pos1[1] - pos2[1])
    z_diff = abs(pos1[2] - pos2[2])

    return x_diff < 2 and y_diff < 2 and z_diff < 2

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

    cube_dict = {}
    x_value = -4
    z_value = -20
    y_value = 0
    player_move_speed = 0.1
    camera_move_speed = 0.3
    player_vertical_speed = 0
    gravity = 0.8
    is_player_grounded = True

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
        x_move = 0
        y_move = 0
        player_move_x = 0
        player_move_y = 0
        player_move_z = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_move = camera_move_speed

        if keys[pygame.K_RIGHT]:
            x_move = -camera_move_speed
        
        if keys[pygame.K_UP]:
            y_move = -camera_move_speed
        
        if keys[pygame.K_DOWN]:
            y_move = camera_move_speed

        if keys[pygame.K_w]:
            player_move_z = -player_move_speed

        if keys[pygame.K_s]:
            player_move_z = player_move_speed

        if keys[pygame.K_a]:
            player_move_x = -player_move_speed

        if keys[pygame.K_d]:
            player_move_x = player_move_speed

        if keys[pygame.K_SPACE] and is_player_grounded:
            is_player_grounded = False
            player_vertical_speed = 10
            player_move_y = player_vertical_speed * 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        glTranslatef(x_move, y_move, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Ground()

        
        player_vertical_speed -= gravity
        player_move_y = player_vertical_speed * 0.1

        current_player_pos = get_vertices(cube_dict[0])
        new_pos_x = current_player_pos[0] + player_move_x
        new_pos_y = current_player_pos[1] + player_move_y
        new_pos_z = current_player_pos[2] + player_move_z

        is_collision_x = False
        is_collision_y = False
        is_collision_z = False
        for each_cube in cube_dict:
            if each_cube != 0 and not is_collision_x and not is_collision_y and not is_collision_z:
                is_collision_x = True if is_collision_x else check_collision([new_pos_x, current_player_pos[1], current_player_pos[2]], get_vertices(cube_dict[each_cube]))
                is_collision_y = True if is_collision_y else check_collision([current_player_pos[0], new_pos_y, current_player_pos[2]], get_vertices(cube_dict[each_cube]))
                is_collision_z = True if is_collision_z else check_collision([current_player_pos[0], current_player_pos[1], new_pos_z], get_vertices(cube_dict[each_cube]))
            Cubes(cube_dict[each_cube])

        if new_pos_y < 0:
            is_player_grounded = True
            player_vertical_speed = 0
            current_player_pos[1] = 0
            new_pos_y = 0

        if not is_collision_y and current_player_pos[1] > 0:
            is_player_grounded = False

        if is_collision_x:
            if player_move_x > 0: new_pos_x = ceil(current_player_pos[0])
            elif player_move_x < 0: new_pos_x = floor(current_player_pos[0])
            else: new_pos_x = current_player_pos[0]

        if is_collision_y:
            if player_move_y < 0:
                is_player_grounded = True
                player_vertical_speed = 0
            if player_move_y > 0: new_pos_y = ceil(current_player_pos[1])
            elif player_move_y < 0: new_pos_y = floor(current_player_pos[1])
            else: new_pos_y = current_player_pos[1]

        if is_collision_z:
            if player_move_z > 0: new_pos_z = ceil(current_player_pos[2])
            elif player_move_z < 0: new_pos_z = floor(current_player_pos[2])
            else: new_pos_z = current_player_pos[2]

        cube_dict[0] = set_vertices(new_pos_x, new_pos_y, new_pos_z)

        Player(cube_dict[0])
        pygame.display.flip()

main()