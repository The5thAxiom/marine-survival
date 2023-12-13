import tkinter as tk
import cv2
from PIL import Image, ImageTk

def ocv2_image_to_tk(image):
    # rearrange colors
    b, g, r = cv2.split(image)
    rearranged_image = cv2.merge((r, g, b))

    # convert into tk format
    pil_image = Image.fromarray(rearranged_image)
    tk_image = ImageTk.PhotoImage(image=pil_image)

    return tk_image

def get_frame(video: cv2.VideoCapture, frame_no: int):
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    return video.read()

current_video_path = '../datasets/video_split_fullhd/DJI_0915_0031_20m.mp4'
current_video = cv2.VideoCapture(current_video_path)
h = int(current_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(current_video.get(cv2.CAP_PROP_FRAME_WIDTH))
current_frame_no: int = 0
current_frame = None
num_frames = int(current_video.get(cv2.CAP_PROP_FRAME_COUNT))

window = tk.Tk()
# window.geometry(f"{w}x{h}")

canvas = tk.Canvas(window, width=w, height=h)
canvas_image = canvas.create_image(0, 0)

def show_current_frame():
    global canvas, canvas_image
    global current_frame

    frame = ocv2_image_to_tk(current_frame)
    canvas.image = frame
    canvas.itemconfig(canvas_image, image=frame)

def manage_frame_controls():
    global current_video, current_frame_no
    global next_button, prev_button, frame_slider, frame_input

    if current_frame_no == 0:
        prev_button['state'] = "disabled"
    else:
        prev_button['state'] = "active"
    if current_frame_no == num_frames:
        next_button['state'] = "disabled"
    else:
        next_button['state'] = "active"

    frame_slider.set(current_frame_no)
    frame_input.delete(0, tk.END)
    frame_input.insert(0, current_frame_no)

def increment_frame():
    global current_frame_no, num_frames
    if current_frame_no < num_frames:
        current_frame_no += 1
        set_current_frame()

def decrement_frame():
    global current_frame_no
    if current_frame_no > 0:
        current_frame_no -= 1
        set_current_frame()

def set_frame_from_slider(event):
    global current_frame_no
    global frame_slider
    current_frame_no = int(frame_slider.get())
    set_current_frame()

def set_frame_from_entry(*args):
    global current_frame_no
    global frame_input_value, frame_input_confirm
    current_frame_no = int(frame_input_value.get())
    set_current_frame()

def manage_frame_input_confirm(*args):
    global current_frame_no
    global frame_input_value, frame_input_confirm
    if frame_input_value.get().isdigit() and int(frame_input_value.get()) != current_frame_no:
        frame_input_confirm['state'] = 'active'
    else:
        frame_input_confirm['state'] = 'disabled'

def set_current_frame():
    global current_frame
    manage_frame_controls()
    no_error, current_frame = get_frame(current_video, current_frame_no)
    if not no_error:
        return
    show_current_frame()


next_button = tk.Button(window, text="Next Frame", command=increment_frame)
prev_button = tk.Button(window, text="Previous Frame", command=decrement_frame)
frame_slider = tk.Scale(window, from_=0, to=num_frames, orient='horizontal', command=set_frame_from_slider, length=w/2)
frame_input_value = tk.StringVar()
frame_input_value.trace("w", manage_frame_input_confirm)
frame_input = tk.Entry(window, textvariable=frame_input_value)
frame_input.bind('<Return>', set_frame_from_entry)
frame_input_confirm = tk.Button(window, text="Set Frame", command=set_frame_from_entry)

set_current_frame()

next_button.pack()
frame_slider.pack()
frame_input.pack()
frame_input_confirm.pack()
prev_button.pack()
canvas.pack()

window.mainloop()