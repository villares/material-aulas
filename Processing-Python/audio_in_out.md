# Usando a biblioteca *Sound* do Processing

É preciso instalar a biblioteca **Sound** da fundação Processing pelo IDE.

### Exemplo se análise do som do microfone

 <sub> Parece que no MacOS Catalina está tendo problema ouvir o microfone</sub>

![](assets/audio_in.gif)

```python
add_library('sound')

def setup():
    global amplitude, amostras, onda
    size(600, 500)
    fonte = AudioIn(this, 0)
    fonte.start()
    amplitude = Amplitude(this)
    amplitude.input(fonte)
    amostras = 60
    onda = Waveform(this, amostras)
    onda.input(fonte)

def draw():
    background(0)
    volume = amplitude.analyze()
    tamanho = volume * 100
    ellipse(300, 200, tamanho, tamanho)
    lista_amostras = onda.analyze()
    for i, a in enumerate(lista_amostras):
        fill(128)
        rect(i * 10, 300, 10, 300 * a)
    
    
```

