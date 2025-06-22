# PY5 IMPORTED MODE CODE

class Botao():

    def __init__(self, x, y, w, h, t):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False

    def mouse_over(self):
        return (self.x < mouse_x < self.x + self.w and
                self.y < mouse_y < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill(140)
        else:
            fill(240)
        rect_mode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t,
             self.x + self.w / 2,
             self.y + self.h / 2)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            return True
        if mouse_over and is_mouse_pressed:
            self.pressed = True
        else:
            self.pressed = False
            
        return False
