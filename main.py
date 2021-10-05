import uvicorn
from fastapi import FastAPI
from joker.controller import joke_controller

app = FastAPI(
    title="The Joker API",
    description="Handle (really) funny jokes",
    version="0.1beta"
)

app.include_router(joke_controller.router, tags=["jokes"])

if __name__ == "__main__":
    uvicorn.run(app)
