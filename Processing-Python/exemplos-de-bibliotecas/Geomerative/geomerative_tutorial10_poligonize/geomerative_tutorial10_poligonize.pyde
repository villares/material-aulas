# ported by Monica Rizzolli

add_library('geomerative')


def setup():
  size(700, 700)
  smooth()
  # VERY IMPORTANT: Allways initialize the library before using it
  RG.init(this);
  global shp

  shp = RG.loadShape("lion.svg")
  shp = RG.centerIn(shp, g, 100)


def draw():
  background(255)

  # We decided the separation between the polygon points dependent of the mouseX
  pointSeparation = map(constrain(mouseX, 100, width-100), 100, width-100, 5, 200)

  # We create the polygonized version
  RG.setPolygonizer(RG.UNIFORMLENGTH);
  RG.setPolygonizerLength(pointSeparation);

  polyshp = RG.polygonize(shp);

  # We move ourselves to the mouse position
  translate(mouseX, mouseY);

  # We draw the polygonized group with the SVG styles
  RG.shape(polyshp);
