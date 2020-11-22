add_library('geomerative')

def setup():
    size(400, 400)
    RG.init(this)

def draw():
    background(100)
    translate(width / 2, height / 2)

    r0 = rg_rect(mouseX, mouseY, 100, 100, QUARTER_PI)
    r1 = rg_rect(mouseX, -mouseY, 100, 100, 0)
    r2 = rg_rect(-mouseX, -mouseY, 100, 100, QUARTER_PI / 2)
    r3 = rg_rect(-mouseX, mouseY, 100, 100)
    noFill()
    RG.shape(r0)
    RG.shape(r1)
    RG.shape(r2)
    RG.shape(r3)
    result = RG.intersection(r0, r1)
    result = RG.intersection(result, r2)
    result = RG.intersection(result, r3)
    fill(255)
    RG.shape(result)


def rg_rect(x, y, w, h, rot=0):
    r = RShape.createRectangle(0, 0, w, h)
    r.translate(x - w / 2, y - h / 2)
    r.rotate(rot, RPoint(x, y))
    return r
