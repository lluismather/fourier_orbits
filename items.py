# item class

import numpy as np


class item:

    def __init__(self, canvas, counter, dims_1, dims_2, centre, radius, recursions, iteration):
        self.CANVAS = canvas
        self.RECURSIONS = recursions
        self.ITERATION = iteration
        self.COUNTER = counter
        self.dims_circle = dims_1
        self.dims_line = dims_2
        self.centre = centre
        self.radius = radius
        self.xy = None
        self.draw_object(self.dims_line, self.dims_circle)
        self.iter_check()

    def draw_object(self, dims_line, dims_circle):
        self.CANVAS.create_line(dims_line, width=1)
        self.CANVAS.create_oval(dims_circle, width=1)
        self.CANVAS.create_oval((self.centre[0] - 1, self.centre[1] - 1, 
                                self.centre[0] + 1, self.centre[1] + 1), width=2)

    def iter_check(self):
        new_counter = self.COUNTER * 5

        if self.ITERATION < self.RECURSIONS:
            self.ITERATION += 1 
            new_radius = (self.radius * 2) * (4 / ((self.ITERATION * 2 + 1) * np.pi))

            xx = (self.centre[0] - self.radius, self.centre[1] - self.radius)
            yy = (self.centre[0] + self.radius, self.centre[1] + self.radius)
            xy = (self.radius * np.cos(1 * new_counter), self.radius * np.sin(1 * new_counter))
            moving_point = (self.centre[0] + xy[0], self.centre[1] + xy[1])

            item(canvas=self.CANVAS, counter=new_counter, dims_1=xx + yy, dims_2=self.centre + moving_point,
                    centre=moving_point, radius=new_radius, recursions=self.RECURSIONS, iteration=self.ITERATION)
        
        else:
            self.CANVAS.create_line((10, 800) + (10, self.centre[1]), width=3)
