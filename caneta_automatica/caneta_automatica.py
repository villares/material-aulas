# -*- coding: utf-8 -*-
# Precisa ter essa linha estranha aí em cima, saiba mais em 
# abav.lugaralgum.com/material-aulas/Processing-Python/modulos
"""
Módulo caneta automática tem funções que lembram a tartaruga da
linguagem Logo, permitem desenhar "arrastando uma caneta".

Crie uma aba chamada caneta_automatica.py e cole este código todo
depois escreva na primeira aba:

from caneta_automatica import *

- Use `size(__, ___)`, com ou sem `def setup():`
- Em seguida chame `inicie_caneta()`

# A caneta começa com o traço ligado
suba_caneta()  # desliga o traço
baixe_caneta()  # volta o traço
ande(passos)  # em pixels
vire(angulo)  # em graus
esquerda()  # 90 graus
direita()  # 90 graus
"""

def inicie_caneta():
    global caneta
    caneta = True  # a caneta começa abaixada
    translate(width / 2, height / 2)
    rotate(HALF_PI)  # rotate(radians(90))

def suba_caneta():
    global caneta
    caneta = False

def baixe_caneta():
    global caneta
    caneta = True

def ande(n):
    if caneta:
        line(0, -n, 0, 0)
    translate(0, -n)

def vire(a):
    rotate(radians(-a))

def esquerda():
    vire(90)

def direita():
    vire(-90)
