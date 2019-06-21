
import tkinter as tk
from tkinter import ttk
from classes import MyCanvas, MyImage
import os

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 560
IMG_WIDTH = 30
IMG_HEIGHT = 30


gui = tk.Tk()
gui.geometry("902x600")
gui.title("Recommender GUI")
gui.resizable(0, 0)

# ----- Canvas -----

canvas = MyCanvas(gui, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, background='gray')
canvas.grid(row=2, column=0, columnspan=3)
for i, filename in enumerate(os.listdir('images/raw/')):
    canvas.add_image(img_path=r"images/raw/%s" % filename, id_=i)


# ----- Disliking product -----

dislike_frame = ttk.LabelFrame(gui, text='Dislike product')
dislike_frame.grid(column=0, row=0, sticky=tk.W)

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
    id_ = like_id.get()
    # id_ = int(like_id.get().strip())
    if id_:
        id_ = int(id_.strip())
        like_id.delete(0, tk.END)
        canvas.mv_image = canvas.images[0]
        canvas.move_image(id_)

    # Todo: retrain recommender model


like_btn = ttk.Button(like_frame, text='Like', command=like_action)
like_btn.grid(column=2, row=0)

# ----- Lines -----

line_dislike = canvas.create_line(120, 0, 120, 560, fill='tomato2', dash='-', width=2)
line_like = canvas.create_line(780, 0, 780, 560, fill='lightgreen', dash='-', width=2)

# ----- Train  -----


def train():
    pass


train_btn = ttk.Button(gui, text='Train Recommender', command=train)
train_btn.grid(column=1, row=0)

gui.mainloop()


