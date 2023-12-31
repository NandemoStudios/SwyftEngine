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
    cat_border = newEngine.draw_rect("black", player['x'], player['y'], 70, 70, 2, rot_to_mouse)
    mouse_pos = Engine.get_mouse_position()
    line_to_mouse = newEngine.draw_line("black", player['x']+35, player['y']+35, mouse_pos[0], mouse_pos[1])
    newEngine.draw_text('X: '+str(player['x']), 0, 0, Roboto, 10)
    newEngine.draw_text('Y: '+str(player['y']), 0, 10, Roboto, 10)
    newEngine.draw_slider(100, 100, 180, 120, 1, 100)
    newEngine.step(framerate)
    newEngine.clear_screen("white")

