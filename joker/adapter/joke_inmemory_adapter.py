import random
from typing import List

from pendulum import now

from joker.domain.joke import Joke
from joker.port.joke_provider import JokeProvider

JOKES = [
    {
        "text": "c'est l'histoire de deux pommes de terre qui traversent une route.l'une d'elles se fait écraser et l'autre hurle : oh purée !",
        "rating": 1,
        "id_joke": 1
    },
    {
        "text": "certaines personnes portent un pyjama superman. superman porte un pyjama chuck norris.",
        "rating": 1,
        "id_joke": 2
    }
]


class JokeInMemoryAdapter(JokeProvider):

    def __init__(self):
        self.jokes: List[Joke] = [Joke(**joke, created_at=now()) for joke in JOKES]

    def get_joke(self, id_joke: int) -> Joke:
        return self.jokes[id_joke]

    def get_jokes(self, start: int, limit: int) -> List[Joke]:
        try:
            return self.jokes[start:start + limit]
        except IndexError:
            return self.jokes[-limit:]

    def add_joke(self, joke: Joke):
        self.jokes.append(joke)
