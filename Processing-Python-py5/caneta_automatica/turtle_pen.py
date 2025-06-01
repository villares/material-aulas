# PY5 IMPORTED MODE CODE
# please keep the previous line, it is a special comment for py5!
"""
Módulo turtle_pen tem funções que lembram a tartaruga da
linguagem Logo, permitem desenhar "arrastando uma caneta".

Crie uma aba chamada turtle_pen.py e cole este código todo
depois escreva na primeira aba:

from pen_automatica import *

- Use `size(__, ___)`, com ou sem `def setup():`
- Em seguida chame `start_pen()`

# A caneta começa com o traço ligado
pen_up()  # turn drawing off
pen_down()  # turn drawing off
forward(steps)  # em pixels
turn(angle)  # em graus
left()  # 90 graus
right()  # 90 graus
"""


def start_pen():
    global pen
    pen = True  # a pen começa abaixada
    reset_matrix()
    translate(width / 2, height / 2)
    rotate(HALF_PI)  # rotate(radians(90))


def pen_up():
    global pen
    pen = False


def pen_down():
    global pen
    pen = True


def forward(n):
    if pen:
        line(0, -n, 0, 0)
    translate(0, -n)


def turn(a):
    rotate(radians(-a))


def left():
    turn(90)


def right():
    turn(-90)
