import gui

WIDTH = 800
HEIGHT = 800
FRAMERATE = 0.1 #float(input("framerate: "))
RECURSIONS = 5 #int(input("recursions: "))

window = gui.window(WIDTH, HEIGHT, FRAMERATE, RECURSIONS)
window.update_frames()
