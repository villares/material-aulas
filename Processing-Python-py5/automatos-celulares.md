# Autômatos Celulares (*Celular Automata*)

# O que são os autômatos celulares, de onde veio essa ideia?

Criados inicalmente como ferramentas de exploração teórica/matemática, robôs auto-replicantes imaginados por von Neuman ou crescimento de cristais, mas também uma atividade lúdica, tornada relativamente popular pela coluna do Martin Gardner de recreações matemáticas na revista Scientific America, que apresentou o jogo da vida do Conway, um dos mais famosos conjuntos de regras para simulação de autômatos celulares em plano (2D). Mais recentemente pesquisadores de urbanismo os estudam como uma ferramenta de simulação, aplicando-os na análise da evolução de trechos de cidade, entre outras tentativas de aplicação.

Os autômatos celulares foram pesquisados em profundidade por [Stephen Wolfram](https://www.wolframscience.com/nks/), que desenvolveu um ultra-simplificado sistema de autômatos celulares em uma linha (1D), mas foram também  adotados por artista visuais que se interessam por computação por conta dos padrões interessantes que geram e o impacto da sua evolução (isso de lembrarem elemento vivos).

Neste material didático os olhamos deste ponto de vista, assim como do ponto de vista didático (para quem quer aprender/ensinar programação), exploratório, lúdico e estético. 

### Alguns exemplos
- "Autômato Celular Elementar" de Wolfram(1D)
  - TODO
- Jogo da vida de Conway(*Conway's game of life*)
  - Exemplo do Jogo da vida de Conway com tabuleiro de lista de listas
  - Exemplo do Jogo da vida de Conway com tabuleiro infinito em um conjunto(set) e a biblioteca py5
  - Exemplo do Jogo da vida de Conway com Numpy
  - Estudar exemplo https://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python

#### GoL com lista de listas

```python
"""
The Game of Life is a cellular automaton devised by the British
mathematician John Horton Conway in 1970. It is the best-known example
of a cellular automaton.

Based on Jeremy Douglass' Processing code & Villares Processing Python mode code
https://rosettacode.org/wiki/Conway%27s_Game_of_Life#Processing_Python_mode
"""

cell_size = 5
sample = 1
play = False   # simulation is running
last_cell = 0

def setup():
    global grid, next_grid, rows, cols
    size(800, 800)
    no_stroke()
    rows = height // cell_size
    cols = width // cell_size
    grid = empty_grid()
    next_grid = empty_grid()
    randomize_grid()

    print("Press 'space' to start/stop")
    print("'e' to clear all cells")
    print("'b' demonstrate 'blinker'")
    print("'g' demonstrate glider")
    print("'r' to randomize grid")
    print("'+' and '-' to change speed")

def draw():
    background(0)
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y = j * cell_size
            current_state = grid[i][j]
            fill(255)
            if current_state:
                rect(x, y, cell_size, cell_size)
            if play:
                ngbs_alive = calc_ngbs_alive(i, j)
                result = rule(current_state, ngbs_alive)
                next_grid[i][j] = result

    if play and frame_count % sample == 0 and not is_mouse_pressed:
        step()

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def rule(current, ngbs):
    """ classic Conway's Game of Life rule """
    if ngbs < 2 or ngbs > 3:
        return 0  # dies / dead
    elif ngbs == 3:
        return 1  # born / alive
    else:
        return current  # stays the same (ngbs == 2)

def calc_ngbs_alive(i, j):
    NEIGHBOURS = ((-1, 00), (0o1, 00),  # a tuple describing the neighbourhood of a cell
                  (-1, -1), (00, -1),
                  (0o1, -1), (-1, 0o1),
                  (00, 0o1), (0o1, 0o1))
    alive = 0
    for iv, jv in NEIGHBOURS:
        alive += grid[(i + iv) % cols][(j + jv) % rows]
    return alive

def empty_grid():
    grid = []
    for _ in range(cols):
        grid.append([0] * rows)
    return grid

def randomize_grid():
    from random import choice
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = choice((0, 1))

def key_released():
    global grid, play, sample
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == "g":
        grid[10][10:13] = [0, 1, 0]
        grid[11][10:13] = [0, 0, 1]
        grid[12][10:13] = [1, 1, 1]
    if key == "b":
        grid[10][10:13] = [0, 1, 0]
        grid[11][10:13] = [0, 1, 0]
        grid[12][10:13] = [0, 1, 0]
    if key == " ":
        play = not play
    if str(key) in '+=':
        sample = max(sample - 1, 1)
    if key == '-':
        sample += 1

def mouse_pressed():
    paint()

def mouse_dragged():
    paint()

def paint():
    global last_cell
    i, j = mouse_x // cell_size, mouse_y // cell_size
    p = j * cols + i
    if p != last_cell:
        last_cell = p
        grid[i][j] = (1, 0)[grid[i][j]]
```

#### GoL com tabuleiro infinito

```python
from collections import Counter
from random import randint
import py5

cell_size = 4
current_board = set()

def setup():
    py5.size(512, 512)
    global ox, oy
    ox, oy = py5.width / 2, py5.height / 2
    py5.no_stroke()
    add_cells()

def add_cells():
    for _ in range(500):
        cell = randint(-50, 50), randint(-50, 50)
        current_board.add(cell)
            
def draw():
    py5.translate(ox * cell_size, oy * cell_size)
    py5.background(0)
    for x, y in current_board:
        py5.square(x * cell_size, y * cell_size, cell_size)
    if py5.frame_count % 2 == 0:
        update()
        
def update():
    global current_board
    n_counts = Counter()
    for x, y in current_board:
        n_counts.update(neighbours(x, y))
    next_board = set()
    for cell in n_counts.keys():
        live_n = n_counts[cell]
        if live_n < 2 or live_n > 3:
            continue
        elif live_n == 3:
            next_board.add(cell)
        elif cell in current_board:
            next_board.add(cell)
    current_board = next_board          
            
def neighbours(x, y):    
    neighbourhood = ((-1, 0), (1, 0), (-1, -1), (0, -1),
                     (1, -1), (-1, 1), (0, 1), (1, 1))
    return [((x + i),  (y + j)) for i, j in neighbourhood]
    
    
def mouse_dragged():
    cell = (py5.mouse_x  // cell_size - ox), (py5.mouse_y // cell_size - oy)
    current_board.add(cell)
    
def key_pressed():
    global cell_size, ox, oy
    if py5.key == ' ':
        add_cells()
    elif py5.key == 'a':
        cell_size *= 2
    elif py5.key == 'z' and cell_size > 0.5:
        print(cell_size)
        cell_size /= 2
    elif py5.key_code == py5.UP:
        oy -= 16
    elif py5.key_code == py5.DOWN:
        oy += 16
    elif py5.key_code == py5.LEFT:
        ox -= 16
    elif py5.key_code == py5.RIGHT:
        ox += 16
        
py5.run_sketch()
```

#### GoL com Numpy

```python
# baseado em on https://www.jpytr.com/post/game_of_life/

import py5
import numpy as np
from scipy.signal import convolve2d

board_img = count_img = None
play = True
sample = 10

def setup():
    global status
    py5.size(800, 800)
    py5.no_smooth()
    status = get_init_status((py5.height // 2, py5.width // 2))

def draw():
    global status, board_img, count_img
    py5.scale(2)
    if play and py5.frame_count % sample == 0 and not mouse_pressed:
        status = apply_conways_game_of_life_rules(status)
    board_img = py5.create_image_from_numpy(status * 255, 'L', dst=board_img)
    py5.image(board_img, 0, 0)
    #count_img = py5.create_image_from_numpy(live_neighbors * 32, 'L', dst=count_img)
    #py5.image(count_img, 0, 0) 

def get_init_status(size, initial_prob_life=0.5):
    status = np.random.uniform(0, 1, size=size) <= initial_prob_life
    return status

def apply_conways_game_of_life_rules(status):
    global live_neighbors
    """Applies Conway's Game of Life rules given the current status of the game"""
    live_neighbors = count_live_neighbors(status)
    survive_underpopulation = live_neighbors >= 2
    survive_overpopulation = live_neighbors <= 3
    survive = status * survive_underpopulation * survive_overpopulation
    new_status = np.where(live_neighbors==3, True, survive)  # Born
    return new_status 

def count_live_neighbors(status):
    """Counts the number of neighboring live cells"""
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    return convolve2d(status, kernel, mode='same', boundary="wrap")

py5.run_sketch()
```

## Bibliografia

- SHIFFMAN, Daniel. _Cellular Automata_. In: < https://natureofcode.com/book/chapter-7-cellular-automata/>.

<!-- Versão traduzida do NoC cap 7 https://github.com/villares/material-aulas/blob/db11434439fc166893da4e9f931c95ca3c72137a/Processing-Python-py5/automatos-celulares.md?plain=1#L17 -->
