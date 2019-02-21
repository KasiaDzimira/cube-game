import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from math import floor, ceil

from Ground import Ground
from Player import Player
from Cubes import Cubes


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

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(50, (display[0] / display[1]), 0.01, 150.0)
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


    cubes = Cubes()
    cube_dict[0] = cubes.set_vertices(-5, 0, -20)

    for x in range(7):
        x_value = x_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(8, 12):
        z_value = z_value - 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(13, 14):
        y_value = y_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(15, 18):
        z_value = z_value - 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(19, 21):
        x_value = x_value - 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(22, 23):
        y_value = y_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(24, 27):
        z_value = z_value - 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(28, 30):
        y_value = y_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(31, 34):
        x_value = x_value - 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(35, 36):
        y_value = y_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    for x in range(37, 41):
        z_value = z_value + 2
        cube_dict[x] = cubes.set_vertices(x_value, y_value, z_value)

    object_passed = False

    while not object_passed:
        x_move = 0
        y_move = 0
        player_move_x = 0
        player_move_y = 0
        player_move_z = 0
        should_reset = False

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

        if keys[pygame.K_r]:
            should_reset = True

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

        ground = Ground()
        ground.draw()
        
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
            if (check_collision([new_pos_x, current_player_pos[1], current_player_pos[2]], get_vertices(cube_dict[40]))) or (check_collision([current_player_pos[0], new_pos_y, current_player_pos[2]], get_vertices(cube_dict[40]))) or (check_collision([current_player_pos[0], current_player_pos[1], new_pos_z], get_vertices(cube_dict[40]))):
                should_reset = True

            if each_cube != 0:
                is_collision_x = True if is_collision_x else check_collision([new_pos_x, current_player_pos[1], current_player_pos[2]], get_vertices(cube_dict[each_cube]))
                is_collision_y = True if is_collision_y else check_collision([current_player_pos[0], new_pos_y, current_player_pos[2]], get_vertices(cube_dict[each_cube]))
                is_collision_z = True if is_collision_z else check_collision([current_player_pos[0], current_player_pos[1], new_pos_z], get_vertices(cube_dict[each_cube]))
            cubes.draw(cube_dict[each_cube])

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
            if player_move_y > 0 and current_player_pos[1] % 2 >= 1: new_pos_y = ceil(current_player_pos[1])
            elif player_move_y > 0 and current_player_pos[1] % 2 < 1: new_pos_y = floor(current_player_pos[1])
            elif player_move_y < 0:
                is_player_grounded = True
                player_vertical_speed = 0
                new_pos_y = floor(current_player_pos[1])
            else: new_pos_y = current_player_pos[1]

        if is_collision_z:
            if player_move_z > 0: new_pos_z = ceil(current_player_pos[2])
            elif player_move_z < 0: new_pos_z = floor(current_player_pos[2])
            else: new_pos_z = current_player_pos[2]

        cube_dict[0] = cubes.set_vertices(new_pos_x, new_pos_y, new_pos_z)
        if should_reset: cube_dict[0] = cubes.set_vertices(-5, 0, -20)


        player = Player()
        player.draw(cube_dict[0])
        pygame.display.flip()

main()