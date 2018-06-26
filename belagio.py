Owner = "Kazimierz Piros"
#note to self: https://github.com/vishnubob/python-midi/blob/master for midi file so imports work...
# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import pprint
from mido import*
songname= input("put in name of song followed by the desierd extension")
chunk = 2048
# open up a wave
if songname[-3:] == wav:
    wf = wave.open(songname, 'rb')
elif songname[-3:] == mid:
    midi_file = MidiFile(songname)

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
filetype = input("input the file type:([1]midi/[2]wav)")
print('consider it done')
if filetype == 2:
    wavplay()
elif filetype == 1:
    midiplay()

def midiplay():
    while True:
        i=i+1
        ############################duration prints ############################################
        sys.stdout.write('=== Track {}\n'.format(i))
        for message in track:
            sys.stdout.write('  {!r}\n'.format(message))
            print (dab[-4:-2])#debugging for durrations
            if dab[-4]=='=':#my shitty durration detection lol
                print(dab[-3:-2])
        #############################duration prints############################################
        if i>3000:
            break
        
        
        with mido.open_output(portname) as output:
            try:
                for message in MidiFile(filename).play():
                    print(message)
                    output.send(message)



def wavplay():
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