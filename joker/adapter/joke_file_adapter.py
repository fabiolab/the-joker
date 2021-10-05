import csv
from typing import List

from pendulum import now

from joker.domain.joke import Joke
from joker.port.joke_provider import JokeProvider

JOKES_FILEPATH = "data/jokes.csv"


class JokeFileAdapter(JokeProvider):

    def __init__(self):
        with open(JOKES_FILEPATH, encoding="utf-8") as joke_file:
            reader = csv.reader(joke_file, delimiter=';')
            self.jokes: List[Joke] = [Joke(id_joke=row[0], text=row[1], rating=row[2], created_at=now()) for row in
                                      reader]

    def get_joke(self, id_joke) -> Joke:
        return self.jokes[id_joke]

    def get_jokes(self, start: int, limit: int) -> List[Joke]:
        try:
            return self.jokes[start:limit]
        except IndexError:
            return self.jokes[-limit:]

    def add_joke(self, joke: Joke):
        self.jokes.append(joke)
        with open(JOKES_FILEPATH, "w", encoding="utf-8") as joke_file:
            joke_file.write(joke.text)
