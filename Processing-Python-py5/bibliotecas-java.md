# Como usar bibliotecas feitas para o Processing Java


Muitas das bibliotecas Java feitas para o Processing funcionam com o py5, no Processing IDE você as instalava usando o painel `Manage Libraries...` do IDE, e no antigo *modo Python* se usava uma função `add_library()`, agora é preciso usar esta função ajudante `py5_tools.processing.download_library()` no exemplo abaixo vamos mostrar como instalar e usar *PeasyCam*.

```python
import py5_tools
print(py5_tools.processing.download_library("PeasyCam"))  # o print é opcional, pra ver o resultado
```
Essa instalação da biblioteca precisa ser feita uma vez só.

## Um exemplo com *PeasyCam*

![](https://raw.githubusercontent.com/villares/sketch-a-day/main/2025/sketch_2025_05_17/sketch_2025_05_17.gif)

```python
from itertools import product    

# No module mode esta intrução precisaria acontecer depois de `import py5`
from peasy import PeasyCam   # é preciso descobrir o nome do módulo, neste caso `peasy`

def setup():
    global cam 
    size(512, 512, P3D)
    this = get_current_sketch() # o equivalnete ao `this` do Java
    cam = PeasyCam(this, 400)
    cam.setMinimumDistance(300);
    cam.setMaximumDistance(500);

def draw():
    background(0)
    color_mode(HSB)
    random_seed(1)
    cs = 32
    for i, j, k in product(range(-3, 4), repeat=3):
        x, y, z = i * cs, j * cs, k * cs 
        bs = random_choice((4, 8, 16, 32))
        fill(bs * 4, 255, 150)
        with push_matrix():
            translate(x, y, z)
            box(bs)
    # exemplo do HUD, desenho de emementos ancorados à tela 
    cam.beginHUD()
    fill(255)
    text_size(20)
    text('PeasyCam demo', 15, 15)
    cam.endHUD()
```


