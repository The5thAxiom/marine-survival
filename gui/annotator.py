import tkinter as tk
import json

from video_player import Video

class Annotator:
    def __init__(self, video: Video, format: str='custom', default_file_path: str=None):
        self.video = video
        self.window = self.video.window
        self.canvas = self.video.canvas
        self.format = format
        if default_file_path is not None:
            self.set_file_path(default_file_path)
        self.show_annotations_bv = tk.BooleanVar(value=False)
        self.toggle = tk.Checkbutton(self.window, text="Show Annotations", variable=self.show_annotations_bv, onvalue=True, offvalue=False, command=self.toggle_handler)
        self.annotation_text_sv = tk.StringVar(self.window)
        self.label = tk.Label(self.window, textvariable=self.annotation_text_sv, anchor='w')
        self.video.add_frame_change_handler(self.redraw_annotations)
        self.current_rects = []
        self.current_labels = []
    
    def set_file_path(self, file_path: str):
        self.file_path = file_path
        
        if self.format == 'custom':
            self.load_custom_json()

    def load_custom_json(self):
        with open(self.file_path, 'r') as json_file:
            self.annotations = json.load(json_file)

    '''
    returns a list of annotations of the format:
    {
        "bbox": [x, y, w, h],
        "label": str
    }
    '''
    def get_frame_annotations(self, frame_index: int):
        for fa in self.annotations:
            if fa['frame_index'] == frame_index:
                return fa['annotations']
    
    def draw_frame_annotations(self):
        self.clear_annotations()
        annotations = self.get_frame_annotations(self.video.current_frame_no)
        annotation_text = f'{len(annotations)} objects:'
        for i, an in enumerate(annotations):
            x, y, w, h = an['bbox']
            self.current_rects.append(self.video.canvas.create_rectangle(x, y, x + w, y + h, outline="red", tags=['box']))
            self.current_labels.append(self.video.canvas.create_text(x, y, text=f"{i}. {an['label']}", fill='red', tags=['label']))
            annotation_text += f"\n{i}. {an['label']}"
        self.annotation_text_sv.set(annotation_text)


    def clear_annotations(self):
        self.video.canvas.delete(['box', 'label']) # this alone SHOULD work but wasn't working for some reason
        for rect in self.current_rects:
            self.video.canvas.delete(rect)
        for label in self.current_labels:
            self.video.canvas.delete(label)
        self.annotation_text_sv.set('')
        self.current_rects = []
        self.current_labels = []

    def redraw_annotations(self):
        self.clear_annotations()
        if self.show_annotations_bv.get():
            self.draw_frame_annotations()

    def toggle_handler(self):
        if self.show_annotations_bv.get():
            self.draw_frame_annotations()
        else:
            self.clear_annotations()