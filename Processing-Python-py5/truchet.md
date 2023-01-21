# Módulos ou mosaicos de Truchet

![image](https://user-images.githubusercontent.com/3694604/188502514-5a8412cd-421f-40f1-a845-02d597c386cc.png)

O ladrilhamento, ou tesselação, isto é o recobrimento de superfícies, por um padrão de quadrados decorados com desenhos que não tem simetria rotacional foi explorada pelo padre dominicano francês Sébastien Truchet.

Veremos aqui uma variante dessa ideia usando arcos que, ao que parece, foi popularizada pelo trabalho de Cyril Stanley Smith and Pauline Boucher, [The Tiling Patterns of Sebastien Truchet and the Topology of Structural Hierarchy](https://www.jstor.org/stable/1578535?origin=crossref&seq=1#metadata_info_tab_contents) em um exemplo traduzido para Python inspirado no código para Processing Java do livro [Processing: Creative Coding and Generative Art in Processing 2](https://rd.springer.com/book/10.1007/978-1-4302-4465-3).


```python
# Translated to Processing Python mode from the Java example at
# "Processing: Creative Coding and Generative Art in Processing 2" by Ira Greenberg, Dianna Xu, Deepak Kumar
# And then adapted for Python + py5 (imported mode)

from random import choice

tile_size = 49
rows = 20
cols = 20

tiles = [[None] * rows for _ in range(cols)]
ic = color(100, 125, 0)     # orange # ic = color(100, 125, 0)
oc = color(20, 150, 255)    # blue # oc = color(20, 150, 255)


def setup():
    size(1000, 1000)
    translate(10, 10)
    fill(255, 0, 0)
    for i in range(rows):
        for j in range(cols):
            tiles[i][j] = Tile(j * tile_size, i * tile_size, tile_size, ic, oc)
            color_swap(i, j)
            tiles[i][j].display()


def color_swap(i, j):
    if i > 0 and j == 0:   # first tile of a row, starting from the 2nd row
        # same orientation as tile directly above
        if tiles[i-1][0].orientation == tiles[i][0].orientation:
            # set to opposite coloring of my neighbor above
            tiles[i][0].swapped_colors = not tiles[i-1][0].swapped_colors
        else:
            # set to same coloring of my neighbor above
            tiles[i][0].swapped_colors = tiles[i-1][0].swapped_colors
    if j > 0:  # subsequent tiles in a row, including the first
        # same orientation as tile to the left
        if tiles[i][j-1].orientation == tiles[i][j].orientation:
            # set to opposite coloring of my neighbor to the left
            tiles[i][j].swapped_colors = not tiles[i][j-1].swapped_colors
        else:
            # set to same coloring of my neighbor to the left
            tiles[i][j].swapped_colors = tiles[i][j-1].swapped_colors


class Tile:

    def __init__(self, x, y, w, ic, oc):
        self.x, self.y = x, y  # x, y coords of top left corner of tile
        self.sz = w  # size of tile
        self.ic = ic  # inside – fill of arc if swapColor is False
        # outside – fill of background square if swapColor is False
        self.oc = oc
        self.orientation = choice((0, 1))  # orientation of tile
        # whether we should swap inside and outside colors
        self.swapped_colors = False

    def display(self):
        push_matrix()
        # move to tile's x-y location (upper left corner)
        translate(self.x, self.y)
        no_stroke()
        if self.swapped_colors:
            fill(self.ic)
        else:
            fill(self.oc)
        rect(0, 0, self.sz, self.sz)  # draw background square
        translate(self.sz / 2, self.sz / 2)  # move to the center of the tile
        rotate(self.orientation * PI / 2)  # rotate by the appropriate angle
        translate(-self.sz / 2, -self.sz / 2)  # back to the upper left corner
        stroke(255)
        stroke_weight(5)
        if self.swapped_colors:
            fill(self.oc)
        else:
            fill(self.ic)
        arc(0, 0, self.sz, self.sz, 0, PI / 2)
        arc(self.sz, self.sz, self.sz, self.sz, PI, 3 * PI / 2)
        pop_matrix()

```
