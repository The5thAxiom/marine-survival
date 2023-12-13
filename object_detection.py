import cv2

# model = cv2.CascadeClassifier(cv2.HOGDescriptor_getDefaultPeopleDetector())

model = cv2.HOGDescriptor()
model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect(raw_image):
    global model

    image = raw_image
    found, weights = model.detectMultiScale(image,  winStride=(8, 8))

    return found, weights

'''
    objects = detect(current_frame)
    if len(objects) == 0:
        return
    current_frame_rectangles = []
    for (x, y, h, w) in objects:
        rect = canvas.create_rectangle(x, y, h, w)
        current_frame_rectangles.append(rect)
'''