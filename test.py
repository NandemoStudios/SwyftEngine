import Engine

framerate = 60

newEngine = Engine.Engine(1280, 720)

while newEngine.running:
    newEngine.draw_circle("Red", 20, 20, 20, 5)
    newEngine.draw_rect("Blue", 20, 30, 20, 30, 5)
    newEngine.step(framerate)
    newEngine.clear_screen("white")
