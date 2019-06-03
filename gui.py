
from tkinter import *
import os
import time

root = Tk()

canvas = Canvas(root, width=600, height=500, background='blue')

print(os.getcwd())
img = PhotoImage(file="./images/shoes_01.ppm")
img = img.subsample(10)
item1 = canvas.create_image(200, 20, image=img)
item2 = canvas.create_image(100, 120, image=img)
canvas.pack()


def move_image(x):
    canvas.move(item1, x, 0)
    canvas.move(item2, x * 2, 0)


for i in range(10):
    print("move", i)
    move_image(i)
    root.update()
    time.sleep(0.1)

root.mainloop()


