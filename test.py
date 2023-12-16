import Engine

framerate = 60

newEngine = Engine.Engine(1280, 720)

while newEngine.running:
    newEngine.draw_circle("Red", 20, 20, 20, 5)
    newEngine.step(framerate)
    newEngine.clear_screen("white")
