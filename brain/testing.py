import cv2
from yolo_model import yolo
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    model=yolo()
    ann,res=model.yolo_model(frame)
    cv2.imshow('cam',ann)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()