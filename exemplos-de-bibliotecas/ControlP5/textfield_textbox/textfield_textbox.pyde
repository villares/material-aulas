add_library('controlP5')

def setup():
    global cp5
    size(500, 500)
    cp5 = ControlP5(this)
    f = createFont("Helvetica", 12)

    (cp5.addTextfield('texto')
     .setSize(120, 20)
     .setPosition(50, 50)
     .setFocus(True)
     .setText(u"Insira um texto")
     .setFont(f)
     )

def draw():
    background(0)
    text(cp5.getController('texto').getText(), 200, 50, 200, 200)
