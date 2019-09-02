# window class

import tkinter as tk
from tkinter import messagebox
import objects


class window:

    def __init__(self, width, height, framerate, recursions):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.RECURSIONS = recursions
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.initialise_window()
        self.d = objects.objects(self.HEIGHT, self.WIDTH, self.FRAMERATE, self.canvas, self.RECURSIONS)

    def initialise_window(self):

        def func_message():
            messagebox.showinfo(title="engine", message="You have opened something.")

        def quitting():
            self.window_active = False

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=quitting)
        menubar.add_cascade(label="File", menu=filemenu)

    def update_frames(self):
        self.d.update_frames()