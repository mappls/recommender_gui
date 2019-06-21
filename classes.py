import tkinter as tk
import numpy as np
import time


class MyImage:

    def __init__(self, path, id):
        self.path = path
        self.id = id


class MyCanvas(tk.Canvas):

    def __init__(self, master, height, width,  **kwargs):

        # Call constructor of parent class
        kwargs['height'] = height
        kwargs['width'] = width
        super().__init__(master=master, **kwargs)

        self.images = []
        self.created_images = []
        self.gui = master
        self.height = height
        self.width = width
        self.mv_image = None
        self.ids = []

    def add_image(self, img_path, id_):
        img_ = tk.PhotoImage(file=img_path)
        img_ = img_.subsample(3)
        self.images.append(img_)
        y = np.random.randint(1, self.height)
        x = self.width // 2
        self.created_images.append(self.create_image(x, y, image=self.images[len(self.images)-1]))
        self.ids.append(self.create_text((x, y), text=id_, fill='red'))

    def move_image(self, id_):
        print('len(images):', len(self.images))
        for i in range(10):
            print("move", i)
            self._move_image(i, id_)
            self.gui.update()
            time.sleep(0.1)

    def _move_image(self, x, id_):
        self.move(self.created_images[id_], x, 0)
        self.move(self.ids[id_], x, 0)

