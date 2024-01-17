import tkinter as tk

class Tabs:
    def __init__(self, window: tk.Tk, tabs_list: list[dict], orient='horizontal'):
        self.window = window
        self.tabs_list = tabs_list
        self.orientation = orient

        self.tabs_frame = tk.Frame(self.window)
        self.tab_buttons_list = [
            tk.Button(
                self.tabs_frame,
                text=tab['name'],
                command=self.tab_button_handler(tab_index)
            ) for tab_index, tab in enumerate(self.tabs_list)
        ]
        self.main = None
        for button in self.tab_buttons_list:
            button.pack(side=tk.LEFT)
        self.set_active_tab(0)

    def _set_ui(self):
        for i, button in enumerate(self.tab_buttons_list):
            if i == self.active_tab_index:
                button['state'] = 'disabled'
                button.config(relief='sunken')
            else:
                button['state'] = 'normal'
                button.config(relief='raised')
        self.tabs_frame.pack(side=tk.TOP, fill=tk.X)
        if self.main is not None and self.main.winfo_manager():
            self.main.pack_forget()
        self.main = self.tabs_list[self.active_tab_index]['widget']
        self.main.pack(side=tk.BOTTOM, expand=True)
    
    def tab_button_handler(self, tab_index=None):
        return lambda: self.set_active_tab(tab_index)
    
    def set_active_tab(self, tab_index: int):
        self.active_tab_index = tab_index
        self._set_ui()