import random

class Horse:
    def __init__(self, name="bob", color="blue"):
        self._name = name
        self._color = color
        self._position = 0

    def move(self):
        num = random.randint(1, 6)
        print(f"{self._name} moved {num} spaces")
        self._position += num