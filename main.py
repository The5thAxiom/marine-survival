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
    ret, frame = video.read()
    if not ret:
        return False, None
    return True, ocv2_image_to_tk(frame)

current_video_path = '../datasets/video_split_fullhd/DJI_0804_0001_30m_1.mp4'
current_video = cv2.VideoCapture(current_video_path)
h = int(current_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(current_video.get(cv2.CAP_PROP_FRAME_WIDTH))
current_frame_no: int = 0

window = tk.Tk()
# window.geometry(f"{w}x{h}")

canvas = tk.Canvas(window, width=w, height=h)
canvas_image = canvas.create_image(0, 0)

def show_current_frame():
    global canvas
    global canvas_image
    global current_frame_no
    global current_video
    no_error, frame = get_frame(current_video, current_frame_no)
    if no_error:
        canvas.image = frame
        canvas.itemconfig(canvas_image, image=frame)
    else:
        print('error hogyi bhaiya')

def manage_buttons():
    global current_frame_no
    global current_video
    global next_button, prev_button
    if current_frame_no == 0:
        prev_button['state'] = "disabled"
    else:
        prev_button['state'] = "active"
    if current_frame_no == int(current_video.get(cv2.CAP_PROP_FRAME_COUNT)):
        next_button['state'] = "disabled"
    else:
        next_button['state'] = "active"

def increment_frame():
    global current_frame_no
    current_frame_no += 1
    manage_buttons()
    show_current_frame()

def decrement_frame():
    global current_frame_no
    current_frame_no -= 1
    manage_buttons()
    show_current_frame()

next_button = tk.Button(window, text="Next Frame", command=increment_frame)
prev_button = tk.Button(window, text="Previous Frame", command=decrement_frame)

manage_buttons()
show_current_frame()

next_button.pack()
prev_button.pack()
canvas.pack()

window.mainloop()