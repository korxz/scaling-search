# scaling-search
Python FastAPI search

## Requirements
- python3
- uv
- postgresql server to connect or use docker setup

## Pre-requirements
- Copy `.env_template` and save it as `.env`
- Create DB and seed it

## DB
DB is located in `scripts/schema.sql`

### Seed db
Downloand TMDB movie data set from keggle and then pass it as script argument.
```bash
uv run python -m scripts.import_records <full_file_path>
```


## How to run
```bash
  uv run fastapi dev
```