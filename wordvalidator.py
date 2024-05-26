import requests


class WordValidator:
    BASE_URL = ""
    ALPHABET = ""

    @staticmethod
    def validate(word):
        ...


class RuWordValidator(WordValidator):
    BASE_URL = "https://erugame.ru/dictionary/backend.php"
    ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    @classmethod
    def validate(cls, word):
        word = word.upper()
        all_chars_in_alphabet = True
        for char in word:
            if char not in cls.ALPHABET:
                all_chars_in_alphabet = False
                break

        if not all_chars_in_alphabet:
            return False

        resp = requests.get(cls.BASE_URL, {"mode": "new", "word": word})
        if resp.status_code != 200:
            return False

        return resp.json().get("result") == "yes"
