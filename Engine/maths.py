import math
import pygame

def get_angle_to_mouse(position):
    mouse_pos = pygame.mouse.get_pos()
    # a^2 + b^2 = c^2
    # rel_pos_y = a
    # rel_pos_x = b

    delta = pygame.Vector2(mouse_pos - position)
    angle_to_mouse = (math.atan2(delta.y, delta.x) / -2) * 100
    looking_vector = pygame.Vector2((100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse)))
    return angle_to_mouse

def get_distance_to_mouse(x, y):
    mouse_pos = pygame.mouse.get_pos()

    b = mouse_pos[0] - x
    a = mouse_pos[1] - y

    c = math.sqrt((b*b) + (a*a))
    return c

def get_distance_from_point(x1: object, y1: object, x2: object, y2: object) -> object:
    b = x2 - x1
    a = y2 - y1

    c = math.sqrt((b*b) + (a*a))
    return c

def if_overlap(x1, y1, x2, y2, x2size, y2size):
    if x1 >= x2 and x1 <= x2size:
        if y1 >= y2 and y1 <= y2size:
            return True
        else:
            return False
    else:
        return False
