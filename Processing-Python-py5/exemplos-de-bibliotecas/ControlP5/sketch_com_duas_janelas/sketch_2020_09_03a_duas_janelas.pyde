# https://Discourse.Processing.org/t/
# how-to-using-controlp5-in-second-window-using-python-mode/13253/6

# GoToLoop (2019-Aug-19)

add_library('controlP5')

def settings():
    size(150, 150)
    Other()


def setup():
    ControlP5(this).addBang('Main').onClick(bangCallback)


def draw():
    background(0)


def bangCallback(v):
    print v.controller


class Other(PApplet):
    SW_PATH = '--sketch-path='
    MAGENTA = 0xFFff00ff

    def __init__(p):
        switches = Other.SW_PATH + sketchPath(), ''
        PApplet.runSketch(switches, p)


    def settings(p):
        p.size(150, 150)


    def setup(p):
        ControlP5(p).addBang('Other').onClick(bangCallback)


    def draw(p):
        p.background(Other.MAGENTA)
