add_library('sound') 

# Times and levels for the ASR envelope
attackTime = 0.001
sustainTime = 0.1
sustainLevel = 0.3
releaseTime = 0.3

# This is an octave in MIDI notes.
midiSequence = {'0': 60, '1': 61, '2': 62, '3': 63, '4': 64, '5': 65, '6': 66, 
                '7': 67, '8': 68, '9': 69, 'x': 70, 'c': 71, 'v': 72
                }  
nota = None 

def setup():
    global triOsc, env
    size(640, 360)
    background(255)
    # Create triangle wave and start it
    triOsc = TriOsc(this)
    # Create the envelope 
    env = Env(this)

def draw(): 
    global nota
    if nota is not None:
        # midiToFreq transforms the MIDI value into a frequency in Hz which we use to
        # control the triangle oscillator with an amplitute of 0.5
        triOsc.play(midiToFreq(midiSequence[nota]), 0.5)
        # The envelope gets triggered with the oscillator as input and the times and
        # levels we defined earlier
        env.play(triOsc, attackTime, sustainTime, sustainLevel, releaseTime)
        nota = None

def keyPressed():
    global nota
    if str(key) in "0123456789xcv":
        nota = key
    
# This helper functiopm calculates the respective frequency of a MIDI note
def midiToFreq(midi_notation):
    return (2 ** ((midi_notation-69)/12.0)) * 440
