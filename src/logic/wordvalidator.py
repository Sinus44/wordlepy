import time

import bs4
import requests


class WordValidator:
    @classmethod
    def validate(cls, word):
        ...


class RuWordValidator3(WordValidator):
    BASE_URL = "https://erugame.ru/dictionary/backend.php"

    @classmethod
    def validate(cls, word):
        try:
            resp = requests.get(cls.BASE_URL, {"mode": "new", "word": word})

        except Exception as error:
            print(error)
            return None

        if resp.status_code != 200:
            return None

        return resp.json().get("result") == "yes"


class RuWordValidator1(WordValidator):
    BASE_URL = "https://api.openrussian.org/suggestions"

    @classmethod
    def validate(cls, word):
        try:
            resp = requests.get(cls.BASE_URL, {"q": word, "dummy": int(time.time() * 1000), "lang": "en"})

        except Exception as error:
            print(error)
            return None

        if resp.status_code != 200:
            return None

        words = [w["word"]["ru"].replace("'", "").upper() for w in resp.json()["result"]["words"]]

        return word in words


class RuWordValidator2(WordValidator):
    BASE_URL = "https://gramota.ru/poisk"

    @classmethod
    def validate(cls, word):
        try:
            resp = requests.get(cls.BASE_URL, {"query": word, "mode": "slovari"})

        except Exception as error:
            print(error)
            return None

        if resp.status_code != 200:
            return None

        sp = bs4.BeautifulSoup(resp.text, features="html.parser")
        words = [a.text.upper() for a in sp.find_all("a", {"class": "title uppercase"})]
        return word in words


class RuWordValidator(WordValidator):
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

        if word[0] in ["Ы", "Ь", "Ъ"]:
            return False

        validator1 = RuWordValidator1.validate(word)

        if validator1 is not None:
            return validator1
        else:
            print("[VALIDATOR1] При проверке слова произошла ошибка")
            validator2 = RuWordValidator2.validate(word)
            if validator2 is not None:
                return validator2
            else:
                print("[VALIDATOR2] При проверке слова произошла ошибка")
                validator3 = RuWordValidator3.validate(word)
                if validator3 is not None:
                    return validator3
                else:
                    print("[VALIDATOR3] При проверке слова произошла ошибка, будет возвращено True")
                    return True
