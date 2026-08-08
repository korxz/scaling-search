from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionDep

router = APIRouter(prefix="/api/v1/movies", tags=["movies"])

@router.get("/")
async def index(db: SessionDep):
    rows = db.exec(text("SELECT * FROM movies LIMIT 1")).mappings().all()
    return [dict(row) for row in rows]

@router.get("/{movie_id}")
async def get_movie(movie_id: int, db: SessionDep):
    row = db.exec(text("SELECT * FROM movies WHERE id = :movie_id"), {"movie_id": movie_id}).mappings().first()
    if row is None:
        return {"error": "Movie not found"}
    
    return dict(row)