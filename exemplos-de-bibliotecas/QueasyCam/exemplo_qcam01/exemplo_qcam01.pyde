from __future__ import division

add_library('queasycam')

counter = 0

def setup():
    global cam   # não é necessário se não usar cam no draw
    size(400, 400, P3D)
    
    cam = QueasyCam(this)
    cam.sensitivity = 0.5
    cam.speed = 0.1
    perspective(PI/3, float(width) / height, 0.01, 10000)
    
def draw():
    global counter
    background(51)
    counter += 0.005
    
    for x in range(-10, 10):
        for y in range(-10, 10):
            z = noise(x/33 + counter, y/33 + counter) * 50
            pushMatrix()
            translate(x * 5, z, y * 5)
            r = map(x, -10, 10, 100, 255)
            g = map(y, -10, 10, 100, 255)
            b = map(z, 0, 10, 100, 255)
            fill(r, g, b)
            box(1)
            popMatrix()
    
