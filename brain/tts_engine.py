import pyttsx3 as pt
import threading
import time

class TTS:
    def __init__(self):
        self.engine=pt.init()
        self.engine.setProperty('rate',170)
        self.engine.setProperty('volume',1.0)

        self.last_msg=''
        self.last_time=''
        self.min_iterval=3
    
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()