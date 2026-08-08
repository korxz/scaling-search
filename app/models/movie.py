from sqlalchemy import BigInteger, Column, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Field, SQLModel
from datetime import date


def text_array() -> Column:
    # A Column instance binds to a single field, so build a fresh one per column.
    return Column(ARRAY(Text), nullable=False, server_default="{}")

class Movie(SQLModel, table=True):
    __tablename__ = "movies"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    vote_average: float | None     
    vote_count: int | None    
    status: str | None 
    release_date: date | None   
    revenue: int | None = Field(sa_type=BigInteger)
    runtime: int | None    
    adult: bool | None       
    backdrop_path: str | None      
    budget: int | None = Field(sa_type=BigInteger)
    homepage: str | None         
    imdb_id: str | None           
    original_language: str | None   
    original_title: str | None
    overview: str | None
    popularity: float | None       
    poster_path: str | None 
    tagline: str | None 
    genres: list[str] = Field(default_factory=list, sa_column=text_array())
    production_companies: list[str] = Field(default_factory=list, sa_column=text_array())
    production_countries: list[str] = Field(default_factory=list, sa_column=text_array())
    spoken_languages: list[str] = Field(default_factory=list, sa_column=text_array())
    keywords: list[str] = Field(default_factory=list, sa_column=text_array())