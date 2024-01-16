import tkinter as tk

from video_player import Video, VideoControls
from file_picker import FilePicker
from annotator import Annotator
from menubar import create_menubar

window = tk.Tk()
window.state('zoomed')
window.title('Marine Survival Object Detection')

# the header
header = tk.Frame(window)
heading=tk.Label(header, text='Marine Survival Object Detection', font=('Arial', 25))
heading.pack()

# the body
body = tk.Frame(window)

# the main pane
main_pane = tk.Frame(body)

video = Video(main_pane)
video_controls = VideoControls(main_pane, video)
video_file_picker = FilePicker(
    main_pane, 'Video File',
    on_file_change=lambda picker: video.set_video(picker.file_path, fps=30),
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/'
)

video_file_picker.ui.pack()
video_controls.ui.pack()
video.ui.pack()

# the left pane
left_pane = tk.Frame(body)

annotation_file_picker = FilePicker(
    left_pane, 'Annotation File',
    on_file_change=lambda picker: annotator.set_file_path(picker.file_path),
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/'
)
annotator = Annotator(left_pane, video)

annotation_file_picker.ui.pack()
annotator.ui.pack()

# layout of panes
header.pack(fill=tk.X, expand=False)
body.pack(fill=tk.Y, expand=False)
left_pane.pack(side=tk.LEFT, fill=tk.X, expand=False)
main_pane.pack(fill=tk.BOTH, expand=True)

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

window.mainloop()