
import tkinter as tk
from tkinter import ttk
import os
import time

gui = tk.Tk()
# gui.geometry("900x600")
gui.title("Recommender GUI")
gui.resizable(0, 0)


class MyCanvas(tk.Canvas):

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.images = []
        self.images_list = None
        self.img1 = None
        self.img2 = None
        self.gui = master

    def add_image(self, img_path):
        img_ = tk.PhotoImage(file=img_path)
        self.img1 = img_.subsample(10)
        self.img2 = self.create_image(50, 50, image=self.img1)
        # self.gui.update()
        # self.move(a, 50, 50)
        # self.images.append(self.create_image(100, 150, image=img_))
        # self.create_rectangle(25, 25, 50, 180, fill='purple', outline='purple')
        # self.create_text(img_label)

    def move_image(self):
        for i in range(10):
            print("move", i)
            self._move_image(i)
            self.gui.update()
            time.sleep(0.1)

    def _move_image(self, x):
        self.move(self.img2, x, 0)
        # self.move(self.images[1], x, 0)


# Add canvas
canvas = MyCanvas(gui, height=500, width=600, background='gray')
canvas.grid(column=1, row=2)
canvas.add_image(img_path=r"images/shoes_01.ppm")

# img_ = tk.PhotoImage(file="images/shoes_01.ppm")
# img_ = img_.subsample(10)
# canvas.create_image(50, 50, image=img_)
# canvas.create_text(150, 150, text='yo yo')


# ----- Disliking product -----

dislike_frame = ttk.LabelFrame(gui, text='Dislike product')
dislike_frame.grid(column=0, row=0)

dislike_label = ttk.Label(dislike_frame, text="Product ID:")
dislike_label.grid(column=0, row=0)

dislike_entry = tk.StringVar()
dislike_id = ttk.Entry(dislike_frame, width=5, textvariable=dislike_entry)
dislike_id.grid(column=1, row=0)


def dislike_action():
    # Todo: move image to left
    # Todo: retrain recommender model
    text = dislike_id.get().strip()
    dislike_id.delete(0, tk.END)
    pass


dislike_btn = ttk.Button(dislike_frame, text='Dislike', command=dislike_action)
dislike_btn.grid(column=2, row=0)


# ----- Liking product -----

like_frame = ttk.LabelFrame(gui, text='Like product')
like_frame.grid(column=2, row=0, sticky=tk.E)

like_label = ttk.Label(like_frame, text="Product ID:")
like_label.grid(column=0, row=0)

like_entry = tk.StringVar()
like_id = ttk.Entry(like_frame, width=5, textvariable=like_entry)
like_id.grid(column=1, row=0)


def like_action():
    text = dislike_id.get().strip()
    like_id.delete(0, tk.END)
    # Todo: move image to right
    canvas.move_image()
    # Todo: retrain recommender model


like_btn = ttk.Button(like_frame, text='Like', command=like_action)
like_btn.grid(column=2, row=0)

gui.mainloop()


