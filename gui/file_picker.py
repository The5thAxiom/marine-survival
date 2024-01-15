import tkinter as tk
from tkinter import filedialog as tk_fd

'''
`FilePicker.label: tk.Label` => displays the 'name' and the name of the selected file
'''
class FilePicker:
    def __init__(self, window: tk.Tk, name: str, on_file_change=None, opening_directory: str=None, default_file_path:str=None):
        self.window = window
        self.name = name
        self.on_file_change = on_file_change
        self.opening_directory = opening_directory

        # setting up the ui
        self.ui = tk.Frame(self.window)
        self.file_path_sv = tk.StringVar(self.ui, value=default_file_path)
        self.label_text = tk.StringVar(self.ui, value=f'{self.name}: {"No file selected" if default_file_path is None else default_file_path}')
        self.label = tk.Label(self.ui, textvariable=self.label_text)
        self.button = tk.Button(self.ui, text="Change", command=self._prompt_user)

        self.label.pack(side=tk.LEFT)
        self.button.pack(side=tk.RIGHT)

    def _prompt_user(self):
        new_file_path = tk_fd.askopenfilename(initialdir=self.opening_directory)
        if new_file_path is None or new_file_path == '':
            self.label_text.set(f'{self.name}: No file selected')
        else:
            self.file_path_sv.set(new_file_path)
            self.label_text.set(f'{self.name}: {self.file_path_sv.get()}')
            if self.on_file_change is not None:
                self.on_file_change(self)

    def get_file_path(self):
        return self.file_path_sv.get()