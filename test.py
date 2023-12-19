import Engine
import Engine.maths
import pygame

framerate = 60

player = {
    'x': 50,
    'y': 50,
    'angle': 90,
    'speed': 3,
    'walkspeed': 3,
    'sprintspeed': 6
}

Roboto = './_internal/font/Roboto-Regular.ttf'
catimg = './_internal/img/cat.png'

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

    rot_to_mouse = Engine.maths.get_angle_to_mouse(pygame.Vector2(player['x'], player['y']))

    cat = newEngine.draw_image(catimg, 70, 70, player['x'], player['y'], rot_to_mouse)
    newEngine.draw_text('X: '+str(player['x']), 0, 0, Roboto, 10)
    newEngine.draw_text('Y: '+str(player['y']), 0, 10, Roboto, 10)
    newEngine.step(framerate)
    newEngine.clear_screen("white")

