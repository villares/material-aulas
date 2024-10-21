# -*- coding: utf-8 -*-

class Bola:
    def __init__(self, x, y, tam):
        self.x = x
        self.y = y
        self.tam = tam # á
        self.cor = color(random(255),
                         random(255),
                         random(255), 100)
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
    
    def plot(self):
        noStroke()
        fill(self.cor)
        if dist(self.x, self.y,
                mouseX, mouseY) < self.tam / 2:
            stroke(255, 0, 0)
            strokeWeight(10)
        circle(self.x, self.y, self.tam)
        
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > width or self.x < 0:
            self.vx = -self.vx
        if self.y > height or self.y < 0:
            self.vy = -self.vy        
        
        
