from graphics import Window, Point
import random

class Horse:
    def __init__(self, name="bob", color="blue", window=None):
        self._name = name
        self._color = color
        self._position = 0
        self.image = None
        

    def move(self):
        num = random.randint(1, 6)
        print(f"{self._name} moved {num} spaces")
        self._position += num

    def draw_horse(self, point, window=None):
        self.point = point
        self._win = window
        if self._win == None:
            return
        if self._color == "blue":
            print("should be loading a blue horse")
            self.image = self._win.draw_image(self.point, "./horses/blue_horse.gif")
        if self._color == "red":
            print("should be loading a red horse")
            self.image = self._win.draw_image(self.point, "./horses/red_horse.gif")