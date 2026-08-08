from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionDep
from app.models.movie import Movie
from array import array

router = APIRouter(prefix="/api/v1/movies", tags=["movies"])

@router.get("/")
def index(db: SessionDep):
    movies = db.exec(text("SELECT * FROM movies LIMIT 100")).mappings().all()
    return [dict(movie) for movie in movies]

@router.get("/{movie_id}")
def get_movie(movie_id: int, db: SessionDep) -> Movie:
    movie = db.get(Movie, movie_id)
    if movie is None:
        return {"error": "Movie not found"}
    
    return dict(movie)