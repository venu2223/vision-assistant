from yolo_model import yolo
from collections import deque
from speak_module import SpeechManager

class PerceptionEngine:
    def __init__(self):
        self.ymodel=yolo()
        self.speaking=SpeechManager()
        self.distance_history={}


    #this is to identigy direction left or right or in front

    def for_direction(self,x_norm_center):
        if x_norm_center<0.4:
            direction='left'
        elif x_norm_center>0.6:
            direction='right'
        else:
            direction='in front'

        return direction

    #this is for distance near or close or far

    def for_distance(self,box_area,frame_area):
        occupy_ratio=box_area/frame_area
        if occupy_ratio>0.2:
            distance='Very Close'
        elif occupy_ratio>0.1:
            distance='Near'
        else:
            distance='far'
        return distance
    
    #insted of outputing every frame at atime it considers the majority distance in n-frames here '5'

    def smoothed_distnace(self,label,current_distance,buffer_size=5):
        if label not in self.distance_history:
            self.distance_history[label]=deque(maxlen=buffer_size)
        self.distance_history[label].append(current_distance)
        dist=max(set(self.distance_history[label]),key=self.distance_history[label].count)
        return dist
    

    #This is main function which combines directions + distances to detect the real world entities

    def detections(self,frame):
        annoted,results=self.ymodel.yolo_model(frame) #Load the YOLO model
        detections=[]
        h,w,_=frame.shape
        frame_area=h*w
        for box in results[0].boxes:
            class_id=int(box.cls[0]) #to get the class id of the entity
            label=results[0].names[class_id] #the classes lable
            label=label.lower()
            x1,y1,x2,y2=box.xyxy[0] #the labels coordinates
            box_area=(x2-x1)*(y2-y1)
            x_center=(x1+x2)/2
            x_center_norm=x_center/w #normalizing 
            direction=self.for_direction(x_center_norm)
            raw_distance=self.for_distance(box_area,frame_area)
            smooth_distance=self.smoothed_distnace(label,raw_distance)
            
            if self.speaking.allow_speech(label,direction,smooth_distance):
                detections.append({
                    'label':label,
                    'direction':direction,
                    'distance':smooth_distance
                })
        return annoted,detections