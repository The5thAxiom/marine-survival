import tkinter as tk

from video_player import Video, VideoControls
from file_picker import FilePicker
from annotator import Annotator

window = tk.Tk()
window.state('zoomed')

video = Video(
    window,
    # default_video_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/DJI_0804_0001_30m_1.mp4'
)

def video_file_change_handler(picker: FilePicker):
    video.set_video(picker.get_file_path(), fps=30)

video_file_picker = FilePicker(
    window, 'Video File',
    on_file_change=video_file_change_handler,
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/',
    # default_file_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/DJI_0804_0001_30m_1.mp4'
)

def annotation_file_change_handler(picker: FilePicker):
    annotator.set_file_path(picker.get_file_path())

annotation_file_picker = FilePicker(
    window, 'Annotation File',
    on_file_change=annotation_file_change_handler,
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/',
    # default_file_path='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/DJI_0804_0001_30m_1.mp4.json'
)

annotator = Annotator(window, video)

video_controls = VideoControls(window, video)

video_file_picker.ui.pack()
annotation_file_picker.ui.pack()
annotator.ui.pack()
video_controls.ui.pack()
video.ui.pack()

window.mainloop()