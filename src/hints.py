import random


class Hint:
    index = -1
    possible_text = [
        "this is a good hint",
        "this is another good hint",
        "hint 3",
        "hint 4"
    ]

    def __init__(self, results):
        self._text = self.assign_text()

    def __repr__(self):
        return f"Hint: {self._text}"
    

    def calculate_cost(self):
        pass

    def assign_text(self):
        if Hint.index < len(Hint.possible_text):
            Hint.index += 1
            return Hint.possible_text[Hint.index]

    @classmethod
    def shuffle_deck(cls):
        random.shuffle(cls.possible_text)

