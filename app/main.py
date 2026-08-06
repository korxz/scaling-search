from fastapi import FastAPI

from app.api.movie_api import router as movie_router

app = FastAPI()
app.include_router(movie_router)