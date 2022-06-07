import tkinter as tk
from tkinter import ttk
from buttons import Buttons
from imgView import ImgView


class Afficher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.filter_frame = None
        self.brightness_frame = None
        self.contrast_frame = None

        self.title("Image Editor")

        self.btns = Buttons(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.imgg = ImgView(master=self)

        self.btns.pack(pady=10)
        separator1.pack(fill=tk.X, padx=20, pady=5)
        self.imgg.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)


imgEditor = Afficher()
imgEditor.mainloop()