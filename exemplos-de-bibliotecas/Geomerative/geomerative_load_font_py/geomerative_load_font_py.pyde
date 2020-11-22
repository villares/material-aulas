add_library('geomerative')


def setup():
    global grp
    size(600, 600)
    RG.init(this)
    grp = RG.getText("Hello world!", "FreeSans.ttf", 72, CENTER)

def draw():
    background(255)
    translate(width / 2, height / 2)
    grp.draw()
