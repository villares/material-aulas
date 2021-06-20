"""
Processing Sound Library, Example 1

Five sine waves are layered to construct a cluster of frequencies. 
This method is called additive synthesis. Use the mouse position 
inside the display window to detune the cluster.
"""

add_library('sound')    # import processing.sound.*

sineWaves = [] # Array of sines
sineFreq  = [] # Array of frequencies
numSines = 5 # Number of oscillators to use

def setup():    
    size(640, 360)
    background(255)

    for i in range(numSines):
        # Calculate the amplitude for each oscillator
        sineVolume = (1.0 / numSines) / (i + 1)
        # Create the oscillators
        sineWaves.append(SinOsc(this))
        # Start Oscillators
        sineWaves[i].play()
        # Set the amplitudes for all oscillators
        sineWaves[i].amp(sineVolume)
        
    sineFreq[:] = [0] * numSines
    

def draw():
    background(200)
    line(0, mouseY, width, mouseY)
    #Map mouseY from 0 to 1
    yoffset = map(mouseY, 0, height, 0, 1)
    #Map mouseY logarithmically to 150 - 1150 to create a base frequency range
    frequency = pow(1000, yoffset) + 150
    #Use mouseX mapped from -0.5 to 0.5 as a detune argument
    detune = map(mouseX, 0, width, -0.5, 0.5)

    for i in range(numSines): 
        sineFreq[i] = frequency * (i + 1 * detune)
        # Set the frequencies for all oscillators
        sineWaves[i].freq(sineFreq[i])
