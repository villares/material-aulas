def setup():
    size(200, 200)  # pyodide.py

def draw():
    background(200)
    diameter = sin(frame_count / 60) * 50 + 50
    fill("blue")
    ellipse(100, 100, diameter, diameter)
