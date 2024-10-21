add_library('OBJExport') # import nervoussystem.obj.*

record = False

def setup():
    size(400,400,P3D)
# The file with the material/color attributes
# Was provided with the lib example
# I have no idea of how they are generated

def draw():
    global record
    background(255)
    if record :
        obj = createGraphics(10, 10,
                             "nervoussystem.obj.OBJExport",
                             "cube.obj")
        obj.setColor(True)
        obj.beginDraw()
        obj.noFill()
        drawColorCube(obj)
        obj.endDraw()
        obj.dispose()
        record =  False
    
    translate(width/2,height/2)
    scale(20)
    rotateX(PI/6.0)
    rotateY(PI/120.0*frameCount)
    drawColorCube(this.g)


def drawColorCube(pg):
    pg.beginShape(QUADS)
    #top
    pg.fill(255,0,0)
    pg.vertex(-1,-1,1)
    pg.vertex(1,-1,1)
    pg.vertex(1,1,1)
    pg.vertex(-1,1,1)
    #bottom
    pg.fill(0,255,0)
    pg.vertex(-1,-1,-1)
    pg.vertex(-1,1,-1)
    pg.vertex(1,1,-1)
    pg.vertex(1,-1,-1)
    #right
    pg.fill(0,0,255)
    pg.vertex(1,1,1)
    pg.vertex(1,-1,1)
    pg.vertex(1,-1,-1)
    pg.vertex(1,1,-1)
    #left
    pg.fill(0,255,255)
    pg.vertex(-1,1,1)
    pg.vertex(-1,1,-1)
    pg.vertex(-1,-1,-1)
    pg.vertex(-1,-1,1)
    pg.endShape()
    #front
    pg.fill(255,0,255)
    pg.vertex(1,1,1)
    pg.vertex(1,1,-1)
    pg.vertex(-1,1,-1)
    pg.vertex(-1,1,1)
    #back
    pg.fill(255,255,0)
    pg.vertex(1,-1,1)
    pg.vertex(-1,-1,1)
    pg.vertex(-1,-1,-1)
    pg.vertex(1,-1,-1)
    
    pg.endShape()


def keyPressed():
    global record
    if key == 'r':
        record = True
