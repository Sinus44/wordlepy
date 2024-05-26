import json


class History:
    FILE_PATH = "history.json"

    @staticmethod
    def load():
        with open(History.FILE_PATH) as file:
            raw = file.read()

        return json.loads(raw)

    @staticmethod
    def save(games):
        raw = json.dumps(games)
        with open(History.FILE_PATH, "w") as file:
            file.write(raw)

    @staticmethod
    def clear():
        History.save([])

    @staticmethod
    def add_game(game):
        game_dict = {
            "win": game.win,
            "word": game.current_word,
            "field": [[(cell.char, cell.type) for cell in line] for line in game.plane]
        }

        games = History.load()
        games.append(game_dict)
        History.save(games)


if __name__ == "__main__":
    History.save(
        [
            {
                "win": True,
                "word": "КРУЖКА",
                "field": [("К", 4), ("Р", 4), ("У", 4), ("Ж", 4), ("К", 4), ("А", 4)]
            }
        ]
    )

    print(History.load())
