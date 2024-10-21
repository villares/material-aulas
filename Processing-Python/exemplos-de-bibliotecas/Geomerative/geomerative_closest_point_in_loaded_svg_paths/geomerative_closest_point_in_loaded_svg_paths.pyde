# https://discourse.processing.org/t/calculate-distance-from-point-to-closest-point-of-shape/7201/7

add_library('geomerative')

chosen_path = 0
diag_points = True
mouse = RPoint(0, 0)
nearest_point = None


def setup():
    global paths
    size(500, 500)
    RG.init(this)
    myshape = RG.loadShape("lines.svg")
    paths = myshape.getPointsInPaths()  # RPoint [][] paths

def draw():
    background(100, 200, 0)
    text("chosen_path = {}".format(chosen_path), 30, 30)
    for points in paths:
        if points:
            if diag_points:
                for p in points:
                    ellipse(p.x, p.y, 2, 2)
            draw_mouseline()

def draw_mouseline():
    global mouse
    mouse = RPoint(float(mouseX), float(mouseY))
    fill(200, 0, 0)
    if nearest_point:
        line(nearest_point.x, nearest_point.y, mouse.x, mouse.y)
        text(int(min_d), mouse.x + 10, mouse.y - 10)
        circle(nearest_point.x, nearest_point.y, 10)


def mouseDragged():
    global nearest_point
    nearest_point = calc_nearest_point(paths[chosen_path])

def calc_nearest_point(path):
    global min_d
    nearest_point = None
    min_d = 10000
    for i, p in enumerate(path):
        d = p.dist(mouse)
        if d < min_d:
            min_d = d
            nearest_point = p
    return nearest_point

def mouseReleased():
    global nearest_point
    nearest_point = None

def mousePressed():
    global chosen_path
    min_d = 1000
    for i, path in enumerate(paths):
        p = calc_nearest_point(path)
        d = p.dist(mouse)
        if d < min_d:
            min_d = d
            nearest_path = i
    chosen_path = nearest_path

def keyPressed():
    global chosen_path
    chosen_path = (chosen_path + 1) % len(paths)
