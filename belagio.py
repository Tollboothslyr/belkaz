Owner = "Kazimierz Piros"
#note to self: https://github.com/vishnubob/python-midi/blob/master for midi file so imports work...
# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import pprint
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,500))
white = (255,255,255)
black = (0,0,0)
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
one = 0
two = 0
three = 0
four = 0
five = 0
lst = []
for yy in range(0,100):
    lst.append(0)
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
        print ("The freq is %f Hz." % (thefreq))
        screen.fill(white)
        if thefreq > 0:
            thefre = (one+two+thefreq+three+four)/6
            for xx in range(0,len(lst)):
                lst[xx] = np.sin((xx-50)*np.tanh(thefre/500)/2)*100
            for xy in range(0,len(lst)):
                pygame.draw.rect(screen,black,(xy*10,500,10,lst[xy]-250))
            pygame.display.update()
            five = four
            four = three
            three = two
            two = one
            one = thefreq
            
            
        
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
