import random
from typing import List

from fastapi import Depends

from joker.dependencies import get_joke_adapter
from joker.port.joke_provider import JokeProvider
from joker.domain.joke import Joke
from joker.port.joke_service_port import JokeServicePort


class JokeService(JokeServicePort):

    def __init__(self, source: JokeProvider = Depends(get_joke_adapter)):
        self.source: JokeProvider = source

    def get_joke(self, id_joke: int) -> Joke:
        return self.source.get_joke(id_joke)

    def get_jokes(self, start: int, limit: int) -> List[Joke]:
        return self.source.get_jokes(start, start + limit)

    def get_random_joke(self) -> Joke:
        return random.choice(self.source.get_jokes(0, 100))

    def add_joke(self, joke: Joke):
        self.source.add_joke(joke)
