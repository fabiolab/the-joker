from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Joke(BaseModel):
    id_joke: int
    text: str
    rating: int = Field(default=0, ge=0, le=5)
    created_at: Optional[datetime]
