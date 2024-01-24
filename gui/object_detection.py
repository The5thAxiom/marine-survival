from ultralytics import YOLO

yolov8 = YOLO('yolov8m.pt')

def detect(image):
    res = yolov8(image)
    return res[0]
