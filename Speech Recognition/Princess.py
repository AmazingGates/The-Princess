import speech_recognition as sr # First we import the proper package and give it a name we can use
import time
import pyttsx3 # This is will make it possible for our assistant to talk back
import pywhatkit # This will allow princess to search youtube for us
import datetime # This package gives us access to time and date information
import wikipedia # This package allows to search wikipedia
import pyjokes # This package gives us access to jokes
import sys
import matplotlib.pyplot as plt
import numpy as np


listener = sr.Recognizer() # This is where we will put our voice recognizer which will understand our voice
engine = pyttsx3.init() # This is where we will create and initialize the engine that will speak back to us 
voices = engine.getProperty("voices") # This is how we catch the pitch of the assistance voice
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_commnad():
# In case we have errors with our microphone or audio, we will use a try and except block
    try:
        with sr.Microphone() as source: # Inside the try block we will use the sr.Microphone and give it a new name
            print("listening......") # This will give us an indicator of when we can speak
            #of source. This will be the source of our audio or source of our commands
            voice = listener.listen(source) # This is where we will declare a variable and this will be the voice and 
            #we will write listener to listen to this source. Once we have this source, we can use the functions 
            #that speech recognization has to convert voice to text. We will use one here.
            command = listener.recognize_google(voice) # This is where we will use our convert voice to text function 
            #and declare it with a variable. We will pass voice as the audio to google() and google will give us the text
            # To make sure this working, we need to print command 
            command = command.lower()
            if "princess" in command:
                command = command.replace("princess", "")
                #print(command) # Instead of print, we can also use a talk(). This will allow the program to speak 
                #the results instead of printing them 
                           
    except:
        pass # This will tell python to ignore whatever exception might happen
    return command


def mandelbrot(c, max_tier):
    z = 0
    for n in range(max_tier):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_tier


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)

    return mset


xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 100

mandlebrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(mandlebrot_image, extent=[xmin, xmax, ymin, ymax], cmap="hot")
plt.colorbar()
plt.title("Mandelbrot Visualization")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
#plt.show()


def run_princess():
    command = take_commnad() # This allows princess to take commands from us.
    #print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song) # Instead of using print, we use the pywhatkit.playonyt() to search and play
        #our song selection on youtbe
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I %M %p") # This will give us access to the curent date and time, and
        #.strftime will let us format the time and date as strings.
        talk("The time is currently" + time)

    elif "tell me about" in command:
        person = command.replace("tell me about", "")
        info = wikipedia.summary(person, 6) # This summary() allows us to choose what we want to search, and how
        #many sentences of information we want returned.
        print(info)
        talk(info)

    elif "joke" in command:
        talk(pyjokes.get_joke()) 

    elif "draw" in command:
        talk("Yes Sir")
        plt.show()

    elif "sleep" in command:
        talk("Until next time Mr. Gates")
        sys.exit()

    else:
        talk("I'm sorry, I don't understand what you are asking me for")

    
while True: # This will make our conversation continue instead of having to keep running the program
    run_princess()
