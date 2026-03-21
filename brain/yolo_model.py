from ultralytics import YOLO

class yolo:
    def __init__(self):
        self.model=YOLO('yolov8s.pt')
    
    #Loading the Yolo model

    def yolo_model(self,frame):
        result=self.model(frame)
        annoted=result[0].plot()
        return annoted,result


