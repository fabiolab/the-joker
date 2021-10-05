from functools import lru_cache

from joker.adapter.joke_file_adapter import JokeFileAdapter
from joker.adapter.joke_inmemory_adapter import JokeInMemoryAdapter
from joker.port.joke_provider import JokeProvider


@lru_cache
def get_joke_adapter() -> JokeProvider:
    return JokeFileAdapter()
