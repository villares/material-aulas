add_library('Unfolding')

def setup():
    global map1
    size(800, 600, P2D)
    smooth()

    map1 = UnfoldingMap(this)
    map1.zoomToLevel(2)
    MapUtils.createDefaultEventDispatcher(this, map1)

    countries = GeoJSONReader.loadData(this, "countries.geo.json")
    country_markers = MapUtils.createSimpleMarkers(countries)
    map1.addMarkers(country_markers)


def draw():
    map1.draw()


def keyPressed():
    if key == ' ':
         map1.getDefaultMarkerManager().toggleDrawing()
