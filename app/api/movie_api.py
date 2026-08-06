from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/movies", tags=["movies"])

@router.get("/")
async def index():
    return {"Hello": "World"}

@router.get("/{movie_id}")
async def get_movie(movie_id: int):
    return {"movie_id": movie_id}