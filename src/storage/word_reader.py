import os


def read_words(file_path, word_length):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("File not found")
        return []

    with open(file_path, "r") as file:
        raw_words = file.read()

    words = raw_words.replace("\n", ",").replace(" ", ",").split(",")
    return [word for word in words if len(word) == word_length]
