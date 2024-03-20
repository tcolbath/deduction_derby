import random


class HintDeck:
    def __init__(self, results):
        self._results = results
        self._index = 0
        self._given_hints = []
        self._possible_text = [
            f"{self._results[0]} came in first"
        ]


    def shuffle_deck(self):
        random.shuffle(self._possible_text)
    

    def draw(self):
        if self._index < len(self._possible_text):
            self._given_hints.append(Hint(self._index, self._possible_text[self._index]))
    
    
class Hint(HintDeck):
    def __init__(self, index, text):
        self._hint_num = index
        self._text = text


    def __repr__(self):
        return f"Hint('{self._text}')"

