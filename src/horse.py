from graphics import Window, Point
import random

class Horse:
    def __init__(self, color="blue", name="bob", window=None):
        self._name = name
        self._color = color
        self._position = 0
        self._exhaust = False
        self.image = None
    
    def __repr__(self):
        return f"{self._color} horse -> {self._name}"
        

    def move(self):
        num = random.randint(1, 6)
        if self._exhaust:
            num = 0
            print(f"Double 6's! {self._name} stumbled from exhaustion and moves 0.")
        if num == 6:
            self._exhaust = True
        else:
            self._exhaust = False
        self._position += num

    def draw_horse(self, point, window=None):
        self.point = point
        self._win = window
        if self._win == None:
            return
        if self._color == "blue":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/blue_horse.png")
        if self._color == "green":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/green_horse.png")
        if self._color == "orange":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/orange_horse.png")
        if self._color == "purple":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/purple_horse.png")
        if self._color == "red":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/red_horse.png")
        if self._color == "yellow":
            print(f"{self._name} placed at start")
            self.image = self._win.draw_image(self.point, "./horses/yellow_horse.png")