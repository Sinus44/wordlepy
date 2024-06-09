import random

import cell
import cellcodes
import history
import jsonreader
import wordreader
import wordvalidator


class Game:
    def __init__(self):
        self.words_path = "./userdata/words.txt"
        self.words_size = 6
        self.attempt_count = 5
        self.current_attempt = 0
        self.current_symbol = 0
        self.words = []
        self.plane = []
        self.current_word = ""
        self.ended = True
        self.win = False
        self.settings = {}
        self.save_history = True
        self.use_word_validator = True
        self.start()

    def start(self):
        self.settings = jsonreader.read("userdata/settings.json", {})
        self.save_history = self.settings.get("save_history", True)
        self.use_word_validator = self.settings.get("use_word_validator", True)
        self.ended = False
        self.win = False
        self.current_attempt = 0
        self.current_symbol = 0
        self.words = wordreader.read_words(self.words_path, self.words_size)
        self.current_word = random.choice(self.words).upper()
        self.plane = [[cell.Cell() for _ in range(self.words_size)] for _ in range(self.attempt_count)]

    def add_symbol(self, symbol):
        if self.current_symbol < self.words_size:
            self.plane[self.current_attempt][self.current_symbol].char = symbol
            self.current_symbol += 1

    def is_full_string(self):
        return self.current_symbol == self.words_size

    def delete_symbol(self):
        if self.current_symbol > 0 and not self.ended:
            self.plane[self.current_attempt][self.current_symbol - 1].char = ""
            self.plane[self.current_attempt][self.current_symbol - 1].type = cellcodes.EMPTY
            self.current_symbol -= 1

    def get_text(self):
        return "".join([c.char for c in self.plane[self.current_attempt]])

    def get_state_keyboard(self, char):
        t = 0
        for line in self.plane:
            for cel in line:
                if cel.char == char:
                    t = max(t, cel.type)

        return t

    def check(self):
        for i, cel in enumerate(self.plane[self.current_attempt]):
            if cel.char in self.current_word:
                cel.type = cellcodes.IN_WORD

            else:
                cel.type = cellcodes.NO

            if cel.char == self.current_word[i]:
                cel.type = cellcodes.POSITION

        if self.get_text() == self.current_word:
            self.win = True
            self.end()

        return self.ended

    def enter(self):
        if not self.is_full_string():
            return

        if self.use_word_validator:
            if not wordvalidator.RuWordValidator.validate(self.get_text()):
                return

        if not self.check():
            if self.current_attempt < self.attempt_count - 1:
                self.current_attempt += 1
                self.current_symbol = 0
            else:
                self.win = False
                self.end()

    def end(self):
        self.ended = True
        if self.save_history:
            history.History.add_game(self)
