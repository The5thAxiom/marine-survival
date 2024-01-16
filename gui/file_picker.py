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
        self.file_path = default_file_path
        self.label = tk.Label(self.ui)
        self.button = tk.Button(self.ui, command=self._prompt_user)
        self.remove_button = tk.Button(self.ui, text='Remove', command=self.remove_file)

        self.label.pack(side=tk.TOP)
        self.button.pack(side=tk.LEFT)

        self._set_ui()

    def _set_ui(self):
        if self.file_path in [None, '']:
            self.label.config(text=f'{self.name}: No file selected')
            self.remove_button.pack_forget()
            self.button.config(text='Add')
        else:
            self.label.config(text=f'{self.name}: {self.file_path}')
            self.remove_button.pack(side=tk.RIGHT)
            self.button.config(text='Change')

    def _prompt_user(self):
        self.file_path = tk_fd.askopenfilename(initialdir=self.opening_directory)
        self._set_ui()
        if self.on_file_change is not None:
            self.on_file_change(self)

    def remove_file(self):
        self.file_path = None
        self._set_ui()
        if self.on_file_change is not None:
            self.on_file_change(self)