import tkinter as tk
from tkinter import filedialog as tk_fd

'''
`FilePicker.label: tk.Label` => displays the 'name' and the name of the selected file
'''
class FilePicker:
    def __init__(self, window: tk.Tk, name: str, on_file_change=None, default_file_path:str=None):
        self.window = window
        self.name = name
        self.file_path = tk.StringVar(self.window, value=default_file_path)
        self.label_text = tk.StringVar(self.window, value=f'{self.name}: {self.file_path.get()}')
        self.label = tk.Label(self.window, textvariable=self.label_text)
        self.button = tk.Button(self.window, text="Change", command=self._prompt_user)
        self.on_file_change = on_file_change
    
    def _prompt_user(self):
        self.file_path.set(tk_fd.askopenfilename())
        self.label_text.set(f'{self.name}: {self.file_path.get()}')
        if self.on_file_change is not None:
            self.on_file_change(self)

    def get_file_path(self):
        return self.file_path.get()