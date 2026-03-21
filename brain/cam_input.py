import cv2
from distance_direction_detect import PerceptionEngine
from danger_detections import DANGER_OBJECTS
from tts_engine import TTS

engine=PerceptionEngine()
speaker=TTS()
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if not ret:
        break
    annoted,detections=engine.detections(frame)
    for d in detections:
        label,direction,distance=d['label'],d['direction'],d['distance']
        if label in DANGER_OBJECTS:
            msg=f'Please be careful,there is a {label} {distance}'
       #     speaker.speak(msg)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
            print(f'Please be careful,there is a {label} {distance}')
            print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            continue
        msg=f"{label} is {direction} and {distance}"
      #  speaker.speak(msg)
        print('####################################\n')
        print(f"{label} is {direction} and {distance}")
        print('\n###################################')
    cv2.imshow('ESP32 cam',annoted)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()