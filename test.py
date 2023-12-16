import Engine
import pygame

framerate = 60

player = {
    'x': 50,
    'y': 50,
    'speed': 3,
    'walkspeed': 3,
    'sprintspeed': 6
}

newEngine = Engine.Engine(1280, 720)

while newEngine.running:
    keys = newEngine.get_input()
    if keys[pygame.K_a]:
        player['x'] -= player['speed']
    if keys[pygame.K_d]:
        player['x'] += player['speed']
    if keys[pygame.K_s]:
        player['y'] += player['speed']
    if keys[pygame.K_w]:
        player['y'] -= player['speed']
    if keys[pygame.K_LSHIFT]:
        player['speed'] = player['sprintspeed']
    if not keys[pygame.K_LSHIFT]:
        player['speed'] = player['walkspeed']

    newEngine.draw_circle("Red", player['x'], player['y'], 20, 5)
    newEngine.draw_rect("Blue", 20, 30, 20, 30, 5)
    newEngine.draw_text('Hello, world!', 70, 70, 32)
    newEngine.step(framerate)
    newEngine.clear_screen("white")
