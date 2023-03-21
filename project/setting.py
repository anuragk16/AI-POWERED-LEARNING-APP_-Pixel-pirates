from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import numpy as np
import pyttsx3 
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 140)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
