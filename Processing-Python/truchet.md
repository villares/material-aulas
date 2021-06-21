# Módulos ou mosaicos de Truchet

![image](https://user-images.githubusercontent.com/3694604/119920020-f8a0cf80-bf41-11eb-9238-c30eac1efebd.png)

A tesselação (isto é o recobrimento de superfícies) por um padrão de quadrados decorados com desenhos que não tem simetria rotacional foi explorada pelo padre dominicano francês Sébastien Truchet. 

Veremos aqui uma variante dessa ideia usando arcos que, ao que parece, foi popularizada pelo trabalho de Cyril Stanley Smith and Pauline Boucher, [The Tiling Patterns of Sebastien Truchet and the Topology of Structural Hierarchy](https://www.jstor.org/stable/1578535?origin=crossref&seq=1#metadata_info_tab_contents) em um exemplo traduzido para Processing modo Python do original em Processing Java no livro [Processing: Creative Coding and Generative Art in Processing 2](https://rd.springer.com/book/10.1007/978-1-4302-4465-3).


```python
# Translated to Processing Python mode from the Java example at
# "Processing: Creative Coding and Generative Art in Processing 2" by Ira Greenberg, Dianna Xu, Deepak Kumar 

tileSize = 50 # tamanho_grid = 50
rows = 50 # n_linhas = 50
cols = 50 # n_colunas = 50

# grid = [[None] * n_linhas for in _ range(n_colunas)]
tiles = [[None] * rows for _ in range(cols)]
ic = color(100, 125, 0)        # orange # ic = color(100, 125, 0)
oc = color(20, 150, 255)    # blue # oc = color(20, 150, 255)

def setup(): 
    size(1000, 1000)
    smooth()
    for i in range(rows):
        for j in range(cols):
            tiles[i][j] = Tile(j*tileSize, i*tileSize, tileSize, ic, oc)
            colorSwap(i, j)
            tiles[i][j].display()
        
    
def colorSwap(i,j):
    if i > 0 and j == 0:   # first tile of a row, starting from the 2nd row
        # same orientation as tile directly above
        if (tiles[i-1][0].intorient == tiles[i][0].intorient):                    
            # set to opposite coloring of my neighbor above
            tiles[i][0].swapColors = not tiles[i-1][0].swapColors
        else:
            # set to same coloring of my neighbor above
            tiles[i][0].swapColors = tiles[i-1][0].swapColors
        
    if j > 0:  # subsequent tiles in a row, including the first
        # same orientation as tile to the left
        if (tiles[i][j-1].intorient == tiles[i][j].intorient):
            # set to opposite coloring of my neighbor to the left
            
            tiles[i][j].swapColors = not tiles[i][j-1].swapColors
        else:
            # set to same coloring of my neighbor to the left 
            tiles[i][j].swapColors = tiles[i][j-1].swapColors
            
class Tile:

    def __init__(self, x, y, w, ic, oc):
        self.x, self.y = x, y  # x, y coords of top left corner of tile
        self.sz = w  # size of tile
        self.ic = ic  # inside – fill of arc if swapColor is False
        # outside – fill of background square if swapColor is False
        self.oc = oc
        self.orient = random(1, 3)  # orientation of tile
        self.intorient = int(self.orient)  # orientation of tile
        # whether we should swap inside and outside colors
        self.swapColors = False

    def display(self):
        pushMatrix()
        # move to tile's x-y location (upper left corner)
        translate(self.x, self.y)
        noStroke()
        if (self.swapColors):
            fill(self.ic)
        else:
            fill(self.oc)

        rect(0, 0, self.sz, self.sz)  # draw background square

        translate(self.sz / 2, self.sz / 2)  # move to the center of the tile
        rotate(self.intorient * PI / 2)  # rotate by the appropriate angle
        # move back to the upper left corner
        translate(-self.sz / 2, -self.sz / 2)
        stroke(255)
        strokeWeight(3)
        if self.swapColors:
            fill(self.oc)
        else:
            fill(self.ic)
