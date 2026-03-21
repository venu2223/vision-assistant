import time
from danger_detections import Dangers

SPEAK_INTERVAL=0.5

class SpeechManager:
    def __init__(self):
        self.previous_states={}
        self.last_spoken_time=0
        self.danger_detections=Dangers()
    '''
        now it is always give like chair left or right,
        so instead we just say like speak when there is a change
        like chair is left or chair is right.
    '''
    def should_speak_on_change(self,label,direction,distance):
        key=label
        current_pos=(direction,distance)
        previous_pos=self.previous_states.get(key)
        if current_pos!=previous_pos:
            self.previous_states[key]=current_pos
            return True
        return False
    
    #Now instead of speaking every second lets make it speak 2 seconds a time
    def can_speak(self,label):
        present_time=time.time()
        priority=self.danger_detections.check_danger(label)
        if  priority=='danger':
            return True
        if present_time-self.last_spoken_time>SPEAK_INTERVAL:
            self.last_spoken_time=present_time
            return True
        return False
    
    def allow_speech(self,label,direction,distance):
        should_speak=self.should_speak_on_change(label,direction,distance)
        canSpeak=self.can_speak(label)
        return should_speak and canSpeak