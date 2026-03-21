
DANGER_OBJECTS = ["car", "bus", "truck", "stairs", "fire", "knife","dog","cat"]
class Dangers:
    def __init__(self):
        pass

    def check_danger(self,label):
        if label in DANGER_OBJECTS:
            return 'danger'
        return 'normal'
    def any_danger(self,label,distance,direction):
        pass