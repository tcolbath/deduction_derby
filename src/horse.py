from graphics import Window, Point
import random

class Horse:
    def __init__(self, color="blue", name="bob", window=None):
        self._name = name
        self._color = color
        self._position = 0
        self._exhaust = False
        self.image = None
        self._rolls = []


    
    def __repr__(self):
        return f"Horse, {self._color}\t:"
        

    def move(self):
        self._last_roll = random.randint(1, 6)
        if self._exhaust:
            self._last_roll = 0
        if self._last_roll == 6:
            self._exhaust = True
        else:
            self._exhaust = False
        self._position += self._last_roll
        return self._last_roll

    def draw_horse(self, point, window=None):
        self.point = point
        self._win = window
        if self._win == None:
            return
        if self._color == "blue":
            self.image = self._win.draw_image(self.point, "./data/horses/blue_horse.png")
        if self._color == "green":          
            self.image = self._win.draw_image(self.point, "./data/horses/green_horse.png")
        if self._color == "orange":
            self.image = self._win.draw_image(self.point, "./data/horses/orange_horse.png")
        if self._color == "purple":
            self.image = self._win.draw_image(self.point, "./data/horses/purple_horse.png")
        if self._color == "red":
            self.image = self._win.draw_image(self.point, "./data/horses/red_horse.png")
        if self._color == "yellow":
            self.image = self._win.draw_image(self.point, "./data/horses/yellow_horse.png")