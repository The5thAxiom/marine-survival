import tkinter as tk

from video_player import Video, VideoControls
from file_picker import FilePicker
from annotator import Annotator
from menubar import create_menubar

window = tk.Tk()
window.state('zoomed')
window.title('Marine Survival Object Detection')

container = tk.PanedWindow(window, orient=tk.VERTICAL)

# the header pane
header_pane = tk.PanedWindow(container, orient=tk.VERTICAL)
heading=tk.Label(header_pane, text='Marine Survival Object Detection', font=('Arial', 25))
header_pane.add(heading)

# the body pane (lol)
body_pane = tk.PanedWindow(container, orient=tk.HORIZONTAL)

# the main pane
main_pane = tk.PanedWindow(body_pane, orient=tk.VERTICAL)

video = Video(main_pane)
video_controls = VideoControls(main_pane, video)
video_file_picker = FilePicker(
    main_pane, 'Video File',
    on_file_change=lambda picker: video.set_video(picker.file_path, fps=30),
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/videos/'
)

main_pane.add(video_file_picker.ui)
main_pane.add(video_controls.ui)
main_pane.add(video.ui)

# the left pane
left_pane = tk.PanedWindow(body_pane, orient=tk.VERTICAL)

annotation_file_picker = FilePicker(
    left_pane, 'Annotation File',
    on_file_change=lambda picker: annotator.set_file_path(picker.file_path),
    opening_directory='D:/VIT/year4/sem8/Capstone/datasets/MOBDrone/annotations/custom-format/'
)
annotator = Annotator(left_pane, video)

left_pane.add(annotation_file_picker.ui)
left_pane.add(annotator.ui)

# layout of panes
container.pack(fill=tk.BOTH, expand=True)
container.add(header_pane)
container.add(body_pane)

body_pane.add(left_pane)
body_pane.add(main_pane)

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