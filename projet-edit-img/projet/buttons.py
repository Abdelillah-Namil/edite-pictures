from tkinter import Frame, Button, LEFT
from tkinter import filedialog
from filterFrame import FilterFrame
from brightnessFrame import BrightnessFrame
from contrastFrame import ContrastFrame
from cv2 import cv2


class Buttons(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)

        self.new_button = Button(self, text="New")
        self.brightness_button = Button(self, text="Brightness")
        self.contrast_button = Button(self, text="Contrast")
        self.filter_button = Button(self, text="Filter")
        self.clear_button = Button(self, text="Clear")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save As")
        # self.quits_button = Button(self, text="Quits")

        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.brightness_button.bind("<ButtonRelease>", self.brightness_button_released)
        self.contrast_button.bind("<ButtonRelease>", self.contrast_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        # self.quits_button.bind("<ButtonRelease>", self.quits_button_released)


        self.new_button.pack(side=LEFT)
        self.brightness_button.pack(side=LEFT)
        self.contrast_button.pack(side=LEFT)
        self.filter_button.pack(side=LEFT)
        self.clear_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        # self.quits_button.pack(side=LEFT)

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:

            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.imgg.show_image()
                self.master.is_image_selected = True

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def brightness_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.brightness_button:
            if self.master.is_image_selected:
                self.master.brightness_frame = BrightnessFrame(master=self.master)
                self.master.brightness_frame.grab_set()


    def contrast_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.contrast_button:
            if self.master.is_image_selected:
                self.master.contrast_frame = ContrastFrame(master=self.master)
                self.master.contrast_frame.grab_set()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()


    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
               self.master.processed_image = self.master.original_image.copy()
               self.master.imgg.show_image()


# def clear_button_released(self, event):
#         if self.winfo_containing(event.x_root, event.y_root) == self.quits_button:
#             imgEditor.destroy
