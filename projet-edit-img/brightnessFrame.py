from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2


class BrightnessFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.brightness_value = 0
        self.previous_brightness_value = 0

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image

        self.brightness_label = Label(self, text="Brightness")
        self.brightness_scale = Scale(self, from_=0, to_=2, length=250, resolution=0.1, orient=HORIZONTAL)

        self.apply_button = Button(self, text="Apply")
        self.preview_button = Button(self, text="Preview")
        self.cancel_button = Button(self, text="Cancel")

        self.brightness_scale.set(1)

        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.brightness_label.pack()
        self.brightness_scale.pack()
        self.cancel_button.pack(side=RIGHT)
        self.preview_button.pack(side=RIGHT)
        self.apply_button.pack()

    def apply_button_released(self, event):
        self.master.processed_image = self.processing_image
        self.close()

    def show_button_release(self, event):
        self.processing_image = cv2.convertScaleAbs(self.original_image, alpha=self.brightness_scale.get())
        self.show_image(self.processing_image)

    def cancel_button_released(self, event):
        self.close()

    def show_image(self, img=None):
        self.master.imgg.show_image(img=img)

    def close(self):
        self.show_image()
        self.destroy()
