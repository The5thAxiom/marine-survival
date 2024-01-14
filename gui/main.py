import tkinter as tk

from video_player import Video, VideoControls
from file_picker import FilePicker
from annotator import Annotator

window = tk.Tk()
window.state('zoomed')
canvas = tk.Canvas(window)

video = Video(
    window, canvas, 
    default_video_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/DJI_0804_0001_30m_1.mp4'
)

def video_file_change_handler(picker: FilePicker):
    video.set_video(picker.get_file_path(), fps=30)

video_file_picker = FilePicker(
    window, 'Video File',
    on_file_change=video_file_change_handler,
    default_file_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/DJI_0804_0001_30m_1.mp4'
)

def annotation_file_change_handler(picker: FilePicker):
    annotator.set_file_path(picker.get_file_path())

annotation_file_picker = FilePicker(
    window, 'Annotation File',
    on_file_change=annotation_file_change_handler,
    default_file_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/DJI_0804_0001_30m_1.mp4.json'
)

annotator = Annotator(video)
annotator.set_file_path(annotation_file_picker.get_file_path())

video_controls = VideoControls(window, video)

video_file_picker.label.pack()
video_file_picker.button.pack()

annotation_file_picker.label.pack()
annotation_file_picker.button.pack()
annotator.toggle.pack()
annotator.label.pack()

video_controls.next_button.pack()
video_controls.frame_slider.pack()
video_controls.frame_input.pack()
video_controls.frame_input_confirm.pack()
video_controls.prev_button.pack()

video.canvas.pack()

window.mainloop()