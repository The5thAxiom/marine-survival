import tkinter as tk

from video_player import Video, VideoControls
from file_picker import FilePicker
from annotator import Annotator
from menubar import create_menubar

window = tk.Tk()
window.state('zoomed')

video = Video(window)

def video_file_change_handler(picker: FilePicker):
    print(f'setting video: {picker.file_path}')
    video.set_video(picker.file_path, fps=30)

video_file_picker = FilePicker(
    window, 'Video File',
    on_file_change=video_file_change_handler,
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/'
)

def annotation_file_change_handler(picker: FilePicker):
    annotator.set_file_path(picker.file_path)

annotation_file_picker = FilePicker(
    window, 'Annotation File',
    on_file_change=annotation_file_change_handler,
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/'
)

annotator = Annotator(window, video)

video_controls = VideoControls(window, video)

window.title('Marine Survival Object Detection')
tk.Label(window, text='Marine Survival Object Detection', font=('Arial', 25)).pack()

create_menubar(window, {
    'File': [
        {'type': 'command', 'label': 'Change Video File', 'command': video_file_picker._prompt_user},
        {'type': 'command', 'label': 'Change Annotations File', 'command': annotation_file_picker._prompt_user},
        {'type': 'separator'},
        {'type': 'command', 'label': 'Exit', 'command': window.destroy}
    ],
    'About': [
        {'type': 'command', 'label': 'Made By Samridh'}
    ]
})

video_file_picker.ui.pack()

annotation_file_picker.ui.pack()
annotator.ui.pack()

video_controls.ui.pack()
video.ui.pack()

window.mainloop()