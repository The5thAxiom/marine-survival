import tkinter as tk
from tkinter import colorchooser
import json

from video_player import Video

class Annotator:
    def __init__(self, window: tk.Tk,  video: Video, color:str='red', format: str='custom', default_file_path: str=None):
        self.video = video
        self.window = window
        self.canvas = self.video.canvas
        self.color = color
        self.format = format
        if default_file_path is not None:
            self.set_file_path(default_file_path)
        self.video.add_frame_change_handler(self.redraw_annotations)
        self.current_rects = []
        self.current_labels = []
        
        # setting up the UI
        self.ui = tk.Frame(self.window)
        self.show_annotations_bv = tk.BooleanVar(self.ui, value=False)
        self.annotation_text_sv = tk.StringVar(self.ui)
        self.toggle = tk.Checkbutton(self.ui, text="Show Annotations", variable=self.show_annotations_bv, onvalue=True, offvalue=False, command=self.toggle_handler)
        self.label = tk.Label(self.ui, textvariable=self.annotation_text_sv, anchor='w')
        self.color_label = tk.Label(self.ui, text=f'color: ■ {self.color}', fg=self.color)
        self.color_picker_button = tk.Button(self.ui, text='■ Change Color', command=self._ask_user_for_color)
        
        self.toggle.pack()
        self.color_label.pack()
        self.color_picker_button.pack()
        self.label.pack()


    def _ask_user_for_color(self):
        self.set_color(colorchooser.askcolor()[1])
        self.redraw_annotations()

    def set_color(self, color: str):
        self.color = color
        self.color_label.config(text=f'color: ■ {self.color}', fg=self.color)

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