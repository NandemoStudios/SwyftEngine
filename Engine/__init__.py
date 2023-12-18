import pygame
import logging

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(framerate)

    def draw_circle(self, color, x, y, radius, width):
        try:
            center = pygame.Vector2(x, y)
            pygame.draw.circle(self.screen, color, center, radius, width)
        except ValueError:
            logging.error("Error, Either center is not two numbers in a sequence, or the radius is not a number")

    def draw_rect(self, color, x1, y1, x2, y2, width):
        rect_rect = pygame.Rect(x1, y1, x2, y2)
        pygame.draw.rect(self.screen, color, rect_rect, width)

    def draw_text(self, text, x, y, font, font_size):
        newFont = pygame.font.Font(font, font_size)
        self.text = pygame.font.Font.render(newFont, text, 1, 'Black')
        self.screen.blit(self.text, (x, y))

    def draw_image(self, path, x, y, xpos, ypos):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (x, y))
        self.screen.blit(img, (xpos, ypos))

    @staticmethod
    def get_input():
        keys = pygame.key.get_pressed()
        return keys

