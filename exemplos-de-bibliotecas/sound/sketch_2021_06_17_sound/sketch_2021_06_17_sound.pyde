"""
Inspect the frequency spectrum of different simple oscillators.
"""

add_library('sound') 

oscillators = []
current_oscillator = 0
fftBands = 512

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
    # Only play one of the four oscillators, based on mouseY
    mouse_selection = floor(map(mouseY, 0, height, 0, len(oscillators)))
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
    
    
    # Map mouseX from 20Hz to 22000Hz for frequency.
    frequency = map(mouseX, 0, width, 20.0, 22000.0)
    # Update oscillator frequency.
    oscillator.freq(frequency)
    # Draw frequency spectrum.
    background(125, 255, 125)
    fill(255, 0, 150)
    noStroke()
    fft.analyze()
    r_width = width/float(fftBands)
    for i in range( fftBands):
        rect(i * r_width, height, r_width, -fft.spectrum[i] * height)
    
    # Display the name of the oscillator class.
    textSize(32)
    fill(0)
    verticalPosition = map(current_oscillator,
                           -1, len(oscillators),
                           0, height)
    text(oscillator.getClass().getSimpleName(), 0, verticalPosition)
