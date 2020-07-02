coresA = (
          (247, 176, 142),
          (237, 232, 69),
          (156, 229, 234),
          (33, 7, 90),
          (71, 242, 238),
          (190, 231, 232),
          )

coresB = (
          (29, 237, 92),
          (109, 0, 255),
          (220, 0, 220),
          (0, 255, 255),
          (203, 31, 79),
          (249, 250, 97),
          )

coresC = (
          (111, 15, 124),
          (102, 100, 47),
          (47, 102, 99),
          (103, 47, 68),
          (232, 228, 16),
          (255, 255, 255),
          )


def setup():
    sel_cor()
    size(500, 600)
    
def draw():
    background(0)
    for i, rgb in enumerate(cores):
        colorMode(RGB)
        c = color(*rgb)
        fill(c)
        h = hue(c)
        rect(0, i * 100, 100, 100)
        fill(255)
        text("{:.2f}".format(h), 120, 50 + i * 100)
        colorMode(HSB)
        fill(h, 200, 200)
        # fill(255)
        rect(200, i * 100, 100, 100)
        fill(h, 255, 255)
        rect(300, i * 100, 100, 100)
    
     
def sel_cor(i=0):
    global cores
    cores = (coresA, coresB, coresC)[i]

def keyPressed():
    if key == '2':
        sel_cor(2)
    if key == '1':
        sel_cor(1)
    if key == '0':
        sel_cor(0)
    
