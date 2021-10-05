from datetime import datetime
from typing import List, Optional

import starlette
from fastapi import APIRouter, Depends, HTTPException, status
from pendulum import now
from pydantic import BaseModel, Field

from joker.domain.joke import Joke
from joker.domain.joke_service import JokeService
from joker.port.joke_service_port import JokeServicePort

router = APIRouter()


class JokeOut(BaseModel):
    text: str
    rating: int = Field(default=0, ge=0, le=5)
    created_at: Optional[datetime]


class JokeIn(BaseModel):
    text: str
    rating: int = Field(default=0, ge=0, le=5)


class JokeController:
    @staticmethod
    @router.get('/jokes/{id_joke}', response_model=JokeOut)
    def get_joke(id_joke: int, joke_service: JokeServicePort = Depends(JokeService)):
        try:
            return joke_service.get_joke(id_joke)
        except IndexError as e:
            raise HTTPException(status_code=404, detail="Joke not found")

    @staticmethod
    @router.get('/jokes', response_model=List[JokeOut])
    def get_jokes(start: int = 0, limit: int = 10, joke_service: JokeServicePort = Depends(JokeService)):
        return joke_service.get_jokes(start, limit)

    @staticmethod
    @router.post('/jokes', response_model=JokeOut, status_code=starlette.status.HTTP_201_CREATED)
    def add_joke(joke: JokeIn, joke_service: JokeServicePort = Depends(JokeService)):
        new_joke = Joke(id_joke=1, created_at=now(), **joke.dict())
        joke_service.add_joke(new_joke)
        return JokeOut(**new_joke.dict())
