Owner = "Kazimierz Piros"
#note to self: https://github.com/vishnubob/python-midi/blob/master for midi file so imports work...
# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import pprint
import pygame

chunk = 2048
# open up a wave
wf = wave.open('kkb.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)
array = ([1,1],
         [1,0],
         [1,1],
         [0,1])

"""def Sprinkle(trigger):
    #psuedo code here
    if trigger == 1:
        actuator(1)
    else:
        actuator(0)
    if trigger >= 3:
        return -1"""

data = wf.readframes(chunk)

i=0 #start counter (inital value)
while True:#len(data) == chunk*swidth: #this is supposed to fit the song but ya know thigns dont always work that way
    #print("hi")
    i=i+1
    stream.write(data)
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))#*window
    fftData=abs(np.fft.rfft(indata))**2
    which = fftData[1:].argmax() + 1
    if which != len(fftData)-1:
       #print("hi")
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        if thefreq >= 5500:  # random integer idk just there becauee if a song goes that high its a fat no from me dog
            thefreq = 463
        print ("The freq is %f Hz." % (thefreq))

    else:
        thefreq = which*RATE/chunk
        if thefreq >= 5500: #random integer idk just there becauee if a song goes that high its a fat no from me dog
            thefreq = 463
        #print("hi")
        print ("The freq is %f Hz." % (thefreq))
    # read some more data
    data = wf.readframes(chunk)
    if i>3000:
        break
    """if thefreq <350:    #this whole if is temp later on its going to be the level of the spray this is just testing
        indices = [i for i, x in enumerate(array) if x == 1]
        Sprinkle(indices)
    elif thefreq > 350:
        indices = [i for i, x in enumerate(array) if x == 0]
        Sprinkle(indices)   #find all occoureness of 0 in the generated array and sprinkle"""

stream.stop_stream()
stream.close()
p.terminate()
