import csv
import sys
from datetime import date
from sqlalchemy import insert
from sqlmodel import Session
from app.database import engine
from app.models.movie import Movie

BATCH_SIZE = 5_000

# Some overview/keyword cells exceed the 128KB default field limit.
csv.field_size_limit(10 ** 7)

def split_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]

def parse_date(value: str) -> date | None:
    return date.fromisoformat(value) if value else None

def map_to_row(row) -> dict:
    return dict(
        title= row[1],
        vote_average= row[2],
        vote_count= row[3],
        status= row[4],
        release_date= parse_date(row[5]),
        revenue= row[6],
        runtime= row[7],
        adult= True if row[8] == 'True' else False,
        backdrop_path= row[9],
        budget= row[10],
        homepage= row[11],
        imdb_id= row[12],
        original_language= row[13],
        original_title= row[14],
        overview= row[15],
        popularity= row[16],
        poster_path= row[17],
        tagline= row[18],
        genres= split_list(row[19]),
        production_companies= split_list(row[20]),
        production_countries= split_list(row[21]),
        spoken_languages= split_list(row[22]),
        keywords= split_list(row[23]),
    )

def import_records(csv_path: str) -> int:
    """Insert rows in batches, committing per batch so a failure keeps prior work."""
    total = 0

    with open(csv_path, newline='') as csvfile, Session(engine) as session:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        batch = []
        for row in reader:
            batch.append(map_to_row(row))

            if len(batch) >= BATCH_SIZE:
                total += flush(session, batch)
                batch.clear()

        if batch:
            total += flush(session, batch)

    return total

def flush(session: Session, batch: list[dict]) -> int:
    session.exec(insert(Movie), params=batch)
    session.commit()
    return len(batch)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python -m scripts.import_records <path-to-csv>")

    count = import_records(sys.argv[1])
    print(f"done: {count:,} rows")
