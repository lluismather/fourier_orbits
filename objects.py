# objects class

import numpy as np
import time
import items


class objects:

    def __init__(self, height, width, framerate, canvas, recursions):
        self.CANVAS = canvas
        self.HEIGHT = height
        self.WIDTH = width
        self.FRAMERATE = framerate
        self.RECURSIONS = recursions
        self.main_unit = (self.HEIGHT / 4) / (4 / (1 * np.pi))
        self.centre = (self.WIDTH / 2, self.HEIGHT / 2)
        self.counter = 0
        self.draw_objects()

    def set_counter(self):
        if self.counter < 360:
            self.counter += (np.pi / 180) / 10
        else:
            self.counter = 0

    def draw_objects(self):
        xx = ((self.WIDTH - (self.HEIGHT / 2)) / 2, self.HEIGHT - (self.HEIGHT / 4))
        yy = ((self.WIDTH + (self.HEIGHT / 2)) / 2, self.HEIGHT / 4)
        xy = (self.main_unit * np.cos(1 * self.counter), self.main_unit * np.sin(1 * self.counter))
        moving_point = (self.centre[0] + xy[0], self.centre[1] + xy[1])
        new_radius = (self.main_unit / 2) / (4 / (1 * np.pi))
        coords_p1 = (self.centre[0] - self.main_unit, self.centre[1] - self.main_unit)
        coords_p2 = (self.centre[0] + self.main_unit, self.centre[1] + self.main_unit)

        items.item(canvas=self.CANVAS, counter=self.counter, dims_1=coords_p1 + coords_p2, centre=moving_point,
            dims_2=self.centre + moving_point, radius=new_radius, recursions=self.RECURSIONS, iteration=1)

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.CANVAS.delete('all')
            self.set_counter()
            self.draw_objects()
            self.CANVAS.update()
        else:
            self.root.quit



