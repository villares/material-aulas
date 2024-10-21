# import fontastic.*
# import geomerative.*
add_library('Fontastic')
add_library('geomerative')

version = 0
charWidth = 512
fontBuilt = False

def setup():
    global font
    size(600, 400)
    fill(0)

    # always initialize the library in setup
    RG.init(this)

    # load the initial font
    font = RFont("FreeSans.ttf", 150)
    # get the points on the curve's shape
    # set style and segment resultion
    RCommand.setSegmentLength(10)
    RCommand.setSegmentator(RCommand.UNIFORMLENGTH)
    initFont()
    updateFont()


def draw():
    updateFont()
    background(255)
    numberOfLetters = 10;    # the number of letters to display
    for i in range(numberOfLetters):
        pushMatrix()
        translate(width / 2, height / 3)
        scale(charWidth / 1000. / 5.)
        translate(-(numberOfLetters - 1) * charWidth / 2 + i * charWidth, 0)
        translate(-charWidth / 2, charWidth / 2)
        noStroke()
        fill(0, 128, 255)
        renderGlyphSolid(Fontastic.alphabet[i], f)
        popMatrix()

    if fontBuilt:
        pushMatrix()
        textFont(myFont)
        textAlign(CENTER, CENTER)
        fill(0)
        textSize(charWidth / 5.)
        text(str(subset(Fontastic.alphabet, 0, numberOfLetters)), width / 2, height * 0.6)
        popMatrix()
        for i in range(numberOfLetters):
            pushMatrix()
            translate(width / 2, height / 3)
            scale(charWidth / 1000. / 5.)
            translate(-(numberOfLetters - 1) * charWidth / 2 + i * charWidth, 0)
            translate(-charWidth / 2, height * 0.6)
            noStroke()
            fill(0, 128, 255)
            renderGlyphSolid(Fontastic.alphabet[i + 5], f)
            popMatrix()
    
def initFont():
    global f
    # create new Fontastic object
    f = Fontastic(this, "Confetti" + nf(version, 4));
    # add letters to the font, adding glyph shapes
    for c in Fontastic.alphabet:
        # add all uppercase letters from the alphabet
        f.addGlyph(c)
    for c in Fontastic.alphabetLc:
        # add all lowercase letters from the alphabet
        f.addGlyph(c)


# f.setFontFamilyName("Confetti");    # if font has same name, won't be
# loaded twice by Processing during runtime
    f.setAuthor("Andreas Koller")
    f.setVersion("0.1")
    f.setAdvanceWidth(int(charWidth * 1.1))



def updateFont():
    for c in Fontastic.alphabet:
        shp = font.toShape(c)
        pnts = shp.getPoints() # RPoint[] 
        f.getGlyph(c).clearContours()
        for i in range(len(pnts)-1):
            p = pnts[i]
            circleSize = 20
            resolution = 6; # the resolution of a confetti circle
            points = [PVector()]*resolution
            for j in range(resolution):
                angle = TWO_PI/(resolution * 1.) * j
                x = p.x * 5 + sin(angle) * circleSize
                y = -p.y * 5 +    cos(angle) * circleSize
                x += (mouseX - width/2.) / width/2. * noise(i+millis()/1000.) * 2000
                y -= (mouseY - height/2.) / height/2. * noise(i * 2+millis()/1000.) * 2000
                points[j] = PVector(x, y)
            f.getGlyph(c).addContour(points)


def createMyFont():
    global myFont, version, fontBuilt
    f.buildFont() # write ttf file
    # delete all glyph files that have been created while building the font
    f.cleanup()
    fontBuilt = True
    # set the font to be used for rendering
    # print f.getTTFfilename()
    myFont = createFont(f.getTTFfilename(), 200);
    version += 1
    initFont() # and make a new font right away

# A function to preview a glyph in Processing
def renderGlyphSolid(c, f):
    contours = f.getGlyph(c).getContoursArray() # FContour[] 

    for j in range(len(contours)):
        # FPoint[] 
        points = f.getGlyph(c).getContour(j).getPointsArray() 

        if len(points) > 0 : #just to be sure
            # Draw the solid shape in Processing
            beginShape();
            for i, p1 in enumerate(points):
                # p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                if p1.hasControlPoint2() and p2.hasControlPoint1():
                    if i == 0:
                        vertex(points[0].x, -points[0].y)

                    bezierVertex(p1.controlPoint2.x, -p1.controlPoint2.y,
                                             p2.controlPoint1.x, -p2.controlPoint1.y, p2.x, -p2.y)
                else:
                    vertex(p1.x, -p1.y)
            endShape()

def keyPressed():
    if key == 's':
        createMyFont()

    
