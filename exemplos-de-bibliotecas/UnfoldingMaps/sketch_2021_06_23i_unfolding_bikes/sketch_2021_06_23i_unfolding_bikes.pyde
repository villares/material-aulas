add_library('Unfolding')

bikeFile = "bikestats.csv"
bikeDataFile = bikeFile

bikeStations = []  #lista de mini dicionários (cada bike stop é um mini dicionário)
maxBikesAvailable = 0

def setup():
    global maxBikesAvailable, map1
    size(800, 600, P2D)
    smooth()

    # Create interactive map1 centered around London
    map1 = UnfoldingMap(this)
    map1.zoomAndPanTo(12, Location(51.500, -0.118))
    MapUtils.createDefaultEventDispatcher(this, map1)
    map1.setTweening(True)
  
    csv_data = loadTable(bikeDataFile, "header, csv")
    for csv_row in csv_data.rows():   # lê uma linha do CSV por vez
        station = dict()   # mini dict vazio
        station['id'] = csv_row.getInt("ID")    
        station['name'] = csv_row.getString("Name")
        station['bikesAvailable'] = csv_row.getInt("BikesAvailable")
        lat = csv_row.getFloat("Latitude")
        lng = csv_row.getFloat("Longitude")
        station['location'] = Location(lat, lng)  # Classe Location (objeto que repres loc)
        station['showLabel'] = False
        bikeStations.append(station)  # jogando na lista
        
        maxBikesAvailable = max(maxBikesAvailable, station['bikesAvailable'])
  
    println("Loaded " + str(len(bikeStations)) + 
            " bikeStations. Max bikes: " + str(maxBikesAvailable)
            )

def draw():
    map1.draw()
    fill(0, 200)
    rect(0, 0, width, height)
    noStroke()
    
    # Iterate over all bike stations
    for station in bikeStations:
        # Convert geo locations to screen positions
        world_pos = station['location']
        screen_pos = map1.getScreenPosition(world_pos)  # ponto na tela
        # map1 number of free bikes to radius of circle
        s = map(station['bikesAvailable'],
                0, maxBikesAvailable, 1, 50)
        # Draw circle according to available bikes
        noStroke()
        fill(255, 0, 255, 150)
        ellipse(screen_pos.x, screen_pos.y, s, s)        
        if station.get('showLabel'):
            fill(255)
            text(station['name'],
                screen_pos.x - textWidth(station ['name'])/2,
                screen_pos.y)
            
        stroke(255)
    #     for other_station in reversed(bikeStations):
    #         if other_station == station:
    #             break
    #         if station['bikesAvailable'] == 0 or other_station['bikesAvailable'] == 0:
    #             continue
    #         world_pos_other = other_station['location']
    #         if world_pos.getDistance(world_pos_other) < 0.3:
    #             screen_pos_other = map1.getScreenPosition(world_pos_other)
    #             line(screen_pos.x, screen_pos.y, screen_pos_other.x, screen_pos_other.y)
            
    # ponto_a = bikeStations[0]
    # world_pos_a = ponto_a['location']  # lat, long do ponto no mapa/mundo
    # screen_pos_a = map1.getScreenPosition(world_pos_a)  # calcula x, y do ponto na tela
    
    # ponto_b = bikeStations[1]
    # world_pos_b = ponto_b['location']
    # screen_pos_b = map1.getScreenPosition(world_pos_b)
    
    # dist_mundo = world_pos_a.getDistance(world_pos_b)
    # print(dist_mundo)  # em kilômetros
    # stroke(255, 0, 0)
    # line(screen_pos_a.x, screen_pos_a.y, screen_pos_b.x, screen_pos_b.y)


def mouseClicked():
    # Simple way of displaying bike station names. Use markers for single station selection.
    for station in bikeStations:
        # station['showLabel'] = False
        pos = map1.getScreenPosition(station['location'])
        if dist(pos.x, pos.y, mouseX, mouseY) < 10:
            station['showLabel'] = not station['showLabel']
