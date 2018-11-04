Owner = "Kazimierz Piros"
# Read in a WAV and find the freq's

import pyaudio
import wave
import numpy as np
import RPi.GPIO as GPIO
import pygame
import time

relaypin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #looking at this gives me anxiety
GPIO.setup(relaypin,GPIO.OUT)

pygame.init()
screen = pygame.display.set_mode((1000, 500))
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
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
lst = []
data = wf.readframes(chunk)
thefreq = 0 # start
a=[]
s = 0.0
i=0 #start counter (inital value)
while True:#len(data) == chunk*swidth: #this is supposed to fit the song but ya know thigns dont always work that way
    #print("hi")
    i=i+1
    #gpio on
    GPIO.output(relaypin, GPIO.HIGH)
    thefreq1 = [thefreq]
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
        if thefreq:

            print ("The freq is %f Hz." % (thefreq))

    else:
        thefreq = which*RATE/chunk
        if thefreq >= 5500: #random integer idk just there becauee if a song goes that high its a fat no from me dog
            thefreq = 463
        #print("hi")
        print ("The freq is %f Hz." % (thefreq))
    # read some more data
    data = wf.readframes(chunk)

    thefreq1.append(thefreq)
    if thefreq1[0] +10 > thefreq1[1] and thefreq1[0] -10 < thefreq1[1]:   #for bunching up frequencys to have notes be more indivdivualistic
        print("yeet")
        #keep gpio on
    else:
        #turn off gpio
        print("ouff")
        GPIO.output(relaypin, GPIO.LOW)

    if i>3000:
        break
    time.sleep(.16666) #set to half of the bpm of the kkb

stream.stop_stream()
stream.close()
p.terminate()

