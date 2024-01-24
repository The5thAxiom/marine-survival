import tkinter as tk
from ultralytics import YOLO

from video_player import Video

class YOLODetector:
    def __init__(self, window: tk.Tk, video: Video):
        self.window = window
        self.video = video
        self.ui = tk.Frame(self.window)
        self.detect_button = tk.Button(self.ui, text='Detect', command=self.detect_current_frame)
        self.video.add_frame_change_handler(self.remove_detections)
        self.current_rects = []
    
    def detect_current_frame(self):
        res = self.model(self.video.current_frame)[0]
        self.remove_detections()
        for box in res.boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
            print('rect: ', x1, y1, x2, y2)
            self.current_rects.append(self.video.canvas.create_rectangle(x1, y1, x2, y2, outline='red'))
        # for box in res:
        #     x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        #     print('rect', x1, y1, x2, y2)
        #     # self.current_rects.append(self.video.canvas.create_rectangle(x1, y1, x2, y2, outline='red'))
    
    def remove_detections(self):
        for rect in self.current_rects:
            self.video.canvas.delete(rect)
        self.current_rects = []
    
    def set_model_file(self, file_path):
        self.model_path = file_path
        self.model = YOLO(self.model_path)

        self.detect_button.pack()




'''
def draw_frame_annotations(self):
    self.clear_annotations()
    if self.video.current_frame_no > self.video.num_frames:
        return
    annotations = self.get_frame_annotations(self.video.current_frame_no)
    annotation_text = f'{len(annotations)} objects:'
    for i, an in enumerate(annotations):
        x, y, w, h = an['bbox']
        self.current_rects.append(self.video.canvas.create_rectangle(x, y, x + w, y + h, outline=self.color, tags=['box']))
        self.current_labels.append(self.video.canvas.create_text(x, y, text=f"{i}. {an['label']}", fill=self.color, tags=['label']))
        annotation_text += f"\n{i}. {an['label']}"
    self.annotation_text_sv.set(annotation_text)
'''