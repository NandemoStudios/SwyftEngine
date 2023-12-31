import logging
import math

import pygame
from pygame_widgets.slider import Slider


class Engine:
    def __init__(self, x, y):
        self.text = None
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()
        self.running = True

    def quit(self):
        self.running = False

    def clear_screen(self, color):
        try:
            self.screen.fill(color)
        except ValueError:
            logging.error("There was an error with your input")

    def step(self, framerate):
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(framerate)

    def draw_circle(self, color, x, y, radius, width):
        try:
            center = pygame.Vector2(x, y)
            pygame.draw.circle(self.screen, color, center, radius, width)
        except ValueError:
            logging.error("Error, Either center is not two numbers in a sequence, or the radius is not a number")

    def draw_rect(self, color, x1, y1, x2, y2, width, angle):
        rect_rect = pygame.Rect(x1, y1, x2, y2)
        positions = get_rectangle_corners(x2, y2, rect_rect.center, angle)
        # new_rect = pygame.Rect(positions[0][1], positions[0][0], x2, y2)
        pygame.draw.rect(self.screen, color, rect_rect, width)

    def draw_line(self, color, start_x, start_y, end_x, end_y):
        pygame.draw.line(self.screen, color, pygame.Vector2(start_x, start_y), pygame.Vector2(end_x, end_y))

    def draw_text(self, text, x, y, font, font_size):
        newFont = pygame.font.Font(font, font_size)
        self.text = pygame.font.Font.render(newFont, text, 1, 'Black')
        self.screen.blit(self.text, (x, y))

    def draw_image(self, path, x, y, xpos, ypos, angle):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (x, y))
        img = pygame.transform.rotate(img, angle)
        rect = img.get_rect()
        rect.center = ((xpos + (x / 2)), (ypos + (y / 2)))
        img_rect = img.get_rect(center=pygame.Vector2(xpos+(x/2), ypos+(y/2)))
        self.screen.blit(img, img_rect)
        return img

    def draw_slider(self, x1, y1, x2, y2, min_value, max_value):
        slider = Slider(self.screen, x1, y1, x2, y2, min=min_value, max=max_value)
        return slider

    @staticmethod
    def get_input():
        keys = pygame.key.get_pressed()
        return keys


def get_mouse_position():
    return pygame.mouse.get_pos()


def rotate_point(center, point, angle):
    # Convert the angle to radians
    angle_rad = math.radians(angle)

    # Translate the point so that the center is at the origin
    translated_point = (point[0] - center[0], point[1] - center[1])

    # Apply the rotation
    rotated_point = (translated_point[0] * math.cos(angle_rad) - translated_point[1] * math.sin(angle_rad),
                     translated_point[0] * math.sin(angle_rad) + translated_point[1] * math.cos(angle_rad))

    # Translate the point back to its original position
    final_point = (rotated_point[0] + center[0], rotated_point[1] + center[1])

    return final_point

def get_rectangle_corners(xSize, ySize, center, angle):
    half_width = xSize/2
    half_height = ySize/2
    top_left_corner = (center[0] - half_width, center[1] - half_height)
    top_right_corner = (center[0] + half_width, center[1] - half_height)
    bottom_left_corner = (center[0] - half_width, center[1] + half_height)
    bottom_right_corner = (center[0] + half_width, center[1] + half_height)
    rotated_top_left = rotate_point(center, top_left_corner, angle)
    rotated_top_right = rotate_point(center, top_right_corner, angle)
    rotated_bottom_left = rotate_point(center, bottom_left_corner, angle)
    rotated_bottom_right = rotate_point(center, bottom_right_corner, angle)
    points = [rotated_top_left, rotated_top_right, rotated_bottom_left, rotated_bottom_right]
    return points

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.Surface([width, height])
        self.sprite.fill(color)

        self.rect = self.sprite.get_rect()

    def update(self, angle):
        self.sprite = pygame.transform.rotate(self.sprite, angle)
        self.rect = self.sprite.get_rect(center=self.rect.center)
