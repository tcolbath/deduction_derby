import random


class HintDeck:
    def __init__(self, results):
        self._results = results
        self._index = 0
        self._given_hints = []
        self._possible_text = [
                f"{self._results[1]._name} came before {self._results[2]._name} but after {self._results[0]._name}",
                f"{self._results[2]._name} came before {self._results[3]._name} but after {self._results[1]._name}",
                f"{self._results[3]._name} came before {self._results[4]._name} but after {self._results[2]._name}",
                f"{self._results[4]._name} came before {self._results[5]._name} but after {self._results[3]._name}",
                f"{self._results[5]._name} came in last",
                f"On Turn 1, second place moved {self._results[1]._rolls[0]}",
                f"On Turn 4, the winner moves {self._results[0]._rolls[3]}",
                f"The winner finishes on turn {len(self._results[0]._rolls)}",
                f"The sum of the first three finisher's moves after Turn 3 is {sum(self._results[0]._rolls[:2]) + sum(self._results[1]._rolls[:2]) + sum(self._results[2]._rolls[:2])}",
                f"On turn 2, the third place finisher is on {self._results[2]._position}"
        ]


    def shuffle_deck(self):
        random.shuffle(self._possible_text)
    

    def draw(self):
        if self._index < len(self._possible_text):
            self._given_hints.append(Hint(self._index, self._possible_text[self._index]))
            self._index += 1
    

class Hint(HintDeck):
    def __init__(self, index, text):
        self._hint_num = index
        self._text = text


    def __repr__(self):
        return f"Hint: {self._hint_num}. '{self._text}'\n"

