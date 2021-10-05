import abc
from typing import List

from joker.domain.joke import Joke


class JokeProvider:
    @abc.abstractmethod
    def get_joke(self, id_joke: int) -> Joke:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_jokes(self, start: int, limit: int) -> List[Joke]:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_joke(self, joke: Joke):
        raise NotImplementedError()
