import tkinter as tk

def create_menubar(window: tk.Tk, menu: dict):
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    for cascade, commands in menu.items():
        menu = tk.Menu(menubar, tearoff=False)
        for c in commands:
            if c['type'] == 'separator':
                menu.add_separator()
            elif c['type'] == 'command':
                menu.add_command(
                    label=c.get('label'),
                    command=c.get('command'),
                    underline=c.get('underline')
                )
        menubar.add_cascade(
            label=cascade,
            menu=menu
        )

# figure out how to add submenus in this