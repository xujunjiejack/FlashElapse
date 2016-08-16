import tkinter as tk
from tkinter import filedialog


def open_dialog_for_path(user_prompt = "Please choose a file for FlashLapse",
                         path_type = "f"):
    '''The type indicates whether the user wants to return a path for directory or for file
    "f" indicates file and "d" indicates directory'''

    root = tk.Tk()
    root.withdraw()
    path = ask_for_path(user_prompt, path_type)
    return path

def ask_for_path(prompt, path_type):
    '''developer note, if the system is os x, we should use message
    for Linux and Windows, I need to use title = prompt
    '''
    print(prompt)
    if path_type == "f":
        return filedialog.askopenfilename(title = prompt)
    elif path_type == "d":
        return filedialog.askdirectory(title = prompt)


