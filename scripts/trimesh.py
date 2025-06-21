import shapely
import trimesh
import py5_tools

def setup():
    global caixa_furada
    size(500, 500, P3D)
    # Produz a geometria da caixa furada
    circulo = shapely.Point(0, 0).buffer(50)  # circulo a partir de ponto, o buffer é o raio
    circulo_deslocado = shapely.affinity.translate(circulo, 50, 0)  # produz cópia deslocada!
    lua = circulo - circulo_deslocado   # equivale a circulo.difference(circulo_deslocado)
    prisma_lua = trimesh.creation.extrude_polygon(lua, 250)  # extrusão da forma de lua
    prisma_lua.apply_translation((0, 0, -125))  # centraliza o prisma com base em forma de lua
    apply_rotation(prisma_lua, PI/2, direction=(0, 1, 0))  # gira o prisma_lua (modifica a malha!)
    prisma_cruz = translated_box(0, 0, 0, 100, 50, 300).union(translated_box(0, 0, 0, 50, 100, 300))
    furo_central = translated_box(0, 0, 0, 180, 300, 180)
    paredes = translated_box(0, 0, 0, 200).difference(furo_central)  
    caixa_furada = paredes.difference(prisma_lua).difference(prisma_cruz)
    # para exportar um gif animado
    #py5_tools.animated_gif('trimesh_demo.gif', duration=0.05, frame_numbers=range(1, 361, 3))
   
def draw():
    background(0, 100, 100)
    lights()
    translate(width / 2, height / 2)
    rotate_x(PI / 8)
    rotate_y(radians(frame_count))
    fill(200, 200, 0)
    draw_mesh(caixa_furada)
  
def key_pressed():
    if key == 's':
        caixa_furada.export('model.stl')
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)  # modifica a malha!

def translated_box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    mesh = trimesh.creation.box((w, h, d))
    mesh.apply_translation((x, y, z))  # modifica a manha!
    return mesh


def draw_mesh(m):
    """Desenha malha trimesh reduzindo arestas coplanares."""
    import numpy as np
    vs = m.vertices
    bs = m.facets_boundary
    # desenha as faces trianguladas sem as arestas
    push_style()  # para poder reverter o desligamento do traço
    no_stroke()   # desliga o  traço, some com as arestas
    with begin_closed_shape(TRIANGLES):
        vertices(vs[np.concatenate(m.faces)])
    pop_style()
    # desenha apenas as linhas dos limites das facetas
    a, b = np.vstack(bs).T
    lines(np.column_stack((vs[a], vs[b])))