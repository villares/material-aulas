# Usando a biblioteca *Sound* do Processing

É preciso instalar a biblioteca ** Sound ** da fundação Processing pelo IDE.

# Exemplo se análise do som do microfone

<sub > Parece que no MacOS Catalina está tendo problema ouvir o microfone < /sub >

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

# Exemplo de osciladores (geradores de onda) com análise frequência
# grádica (FFT)

```python
# Inspect the frequency spectrum of different simple oscillators.

add_library('sound')

oscillators = []
current_oscillator = 0
fft_bands = 512


def setup():
    global fft
    size(640, 360)
    background(255)

    # Turn the volume down globally.
    s = Sound(this)
    s.volume(0.2)
    # Create the oscillators and put them into an array.
    oscillators.append(SinOsc(this))
    oscillators.append(TriOsc(this))
    oscillators.append(SawOsc(this))
    oscillators.append(SqrOsc(this))
    # Special treatment for the Pulse oscillator to set its pulse width.
    pulse = Pulse(this)
    pulse.width(0.05)
    oscillators.append(pulse)
    # Initialise the FFT and start playing the (default) oscillator.
    fft = FFT(this, 512)
    oscillators[current_oscillator].play()
    fft.input(oscillators[current_oscillator])


def draw():
    global current_oscillator
    # Only play one of the four oscillators, based on mouse_y
    mouse_selection = floor(map(mouse_y, 0, height, 0, len(oscillators)))
    next_oscillator = constrain(mouse_selection, 0, len(oscillators) - 1)
    oscillator = oscillators[current_oscillator]

    if next_oscillator != current_oscillator:
        oscillator.stop()
        current_oscillator = next_oscillator
        oscillator = oscillators[current_oscillator]
        # Switch FFT analysis over to the newly selected oscillator.
        fft.input(oscillator)
        # Play
        oscillator.play()

    # Map mouse_x from 20Hz to 22000Hz for frequency.
    frequency = map(mouse_x, 0, width, 20.0, 22000.0)
    # Update oscillator frequency.
    oscillator.freq(frequency)
    # Draw frequency spectrum.
    background(125, 255, 125)
    fill(255, 0, 150)
    no_stroke()
    fft.analyze()
    r_width = width/float(fft_bands)
    for i in range(fft_bands):
        rect(i * r_width, height, r_width, -fft.spectrum[i] * height)

    # Display the name of the oscillator class.
    text_size(32)
    fill(0)
    vertical_position = map(current_oscillator,
                            -1, len(oscillators),
                            0, height)
    text(oscillator.get_class().get_simple_name(), 0, vertical_position)


```
