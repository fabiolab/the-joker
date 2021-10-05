from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from joker.dependencies import get_joke_adapter
from joker.domain.joke import Joke
from main import app


@pytest.fixture(scope="module")
def test_app():
    return TestClient(app)


def get_joke_mock():
    joke_mock_adapter = MagicMock()
    joke_mock_adapter.get_joke = MagicMock(return_value=Joke(id_joke=1, text="A fake joke", rating=0))
    return joke_mock_adapter


app.dependency_overrides[get_joke_adapter] = get_joke_mock


def test_get_joke(test_app):
    response = test_app.get('/jokes/1')
    assert not response.json().get("id_joke", None)
    assert response.json()["text"] == "A fake joke"
