from collections.abc import Generator
from typing import Annotated
from fastapi import Depends

from sqlmodel import Session, create_engine
from pydantic import PostgresDsn
from .config import settings

def uri() -> PostgresDsn:
    return PostgresDsn.build(
        scheme="postgresql+psycopg",
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        path=settings.DB_PATH,
    )

engine = create_engine(str(uri()))

def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]