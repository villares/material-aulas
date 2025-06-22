"""
Código para a leitura dos potenciômetros, requer biblioteca PyFirmata e arquivo inputs.py
"""

# ARDUINO
POT_AMARELO = 0   # Pino que vai ser lido controle 'jogador Amarelo'
POT_VERDE = 5   # Pino que vai ser lido controle 'jogador Verde'

# JOGADORES
MEIA_ALTURA_JOGADOR = 50  # tamanho de meia altura do jogador
LARGURA_JOGADOR = 10

from inputs import get_arduino

def setup():
    size(600, 400)  # tamanho da tela
    global arduino
    arduino = get_arduino()
    if arduino is None:
        print('Não encontrei um Arduino.')
        exit_sketch()

def draw():
    background(0)  # limpa a tela
    # CÍRCULO AMARELO
    AMARELO_Y = arduino.analog_read(POT_AMARELO) / 2
    fill(255, 255, 0)  # fill(vermelho->255, verde->255, azul->0) -> Amarelo
    ellipse(50,         # x
            50,         # y
            AMARELO_Y,  # largura
            AMARELO_Y)  # altura
    # CÍRCULO VERDE
    VERDE_Y = arduino.analog_read(POT_VERDE) / 2
    fill(0, 255, 0)  # fill(vermelho->0, verde->255, azul->0) -> Verde
    ellipse(width - 50,  # x
            50,          # y
            VERDE_Y,     # largura
            VERDE_Y)     # altura
